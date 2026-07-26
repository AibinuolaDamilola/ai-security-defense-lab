import streamlit as st
import os
import base64
from supabase import create_client, Client

st.set_page_config(page_title="AI Defense Lab", page_icon="🛡️", layout="wide")

st.markdown("""<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
.block-container {padding-top:0rem;}
</style>""", unsafe_allow_html=True)

SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://jpmzgvulaamzuajuicyi.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpwbXpndnVsYWFtenVhanVpY3lpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODAyNTMwNzAsImV4cCI6MjA5NTgyOTA3MH0.6NW-Ov_Un6wqWPbe26Fg2kcq0D2z0wnehkgHav7c3q8")

@st.cache_resource
def init_supabase():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase: Client = init_supabase()

def get_authed_client():
    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    if st.session_state.get("access_token"):
        client.postgrest.auth(st.session_state.access_token)
    return client

ASSETS_DIR = os.path.dirname(__file__)

def load_b64(filename):
    path = os.path.join(ASSETS_DIR, "assets", filename)
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

LAB_LOGO_B64 = load_b64("ai_defense_lab_logo.png")
HN_LOGO_B64  = load_b64("hernetiq_logo.png")

for key, default in [
    ("user", None), ("access_token", None), ("refresh_token", None),
    ("view", "hub"), ("onboarding_step", 0), ("auth_error", ""), ("auth_success", ""),
    ("pending_full_name", ""), ("l1_completed", False),
    ("l2_completed", False), ("l2_scan_run", False),
]:
    if key not in st.session_state:
        st.session_state[key] = default


def do_sign_in(email, password):
    try:
        result = supabase.auth.sign_in_with_password({"email": email, "password": password})
        st.session_state.user          = result.user
        st.session_state.access_token  = result.session.access_token
        st.session_state.refresh_token = result.session.refresh_token
        st.session_state.auth_error    = ""
        st.rerun()
    except Exception as e:
        st.session_state.auth_error = str(e)


def do_sign_up(email, password, full_name):
    try:
        result = supabase.auth.sign_up({"email": email, "password": password})
        if result.user:
            # Store name in session state — will be saved to Supabase during onboarding
            # (sign_up client has no JWT yet so RLS would block a direct update here)
            if full_name:
                st.session_state.pending_full_name = full_name
            st.session_state.auth_success = "Account created! Check your email to confirm, then sign in."
        st.session_state.auth_error = ""
    except Exception as e:
        st.session_state.auth_error = str(e)


def do_sign_out():
    try:
        supabase.auth.sign_out()
    except Exception:
        pass
    for key in ["user", "access_token", "refresh_token"]:
        st.session_state[key] = None
    st.session_state.view = "hub"
    st.session_state.onboarding_step = 0
    st.rerun()


def get_user_profile():
    try:
        result = get_authed_client().table("defense_lab_users").select("*").eq(
            "id", str(st.session_state.user.id)
        ).execute()
        return result.data[0] if result.data else {}
    except Exception:
        return {}


def get_progress():
    try:
        result = get_authed_client().table("defense_lab_progress").select("*").eq(
            "user_id", str(st.session_state.user.id)
        ).order("level_number").execute()
        return {row["level_number"]: row for row in result.data} if result.data else {}
    except Exception:
        return {}


def mark_onboarding_complete():
    try:
        update_data = {"onboarding_complete": True}
        if st.session_state.get("pending_full_name"):
            update_data["full_name"] = st.session_state.pending_full_name
        get_authed_client().table("defense_lab_users").update(
            update_data
        ).eq("id", str(st.session_state.user.id)).execute()
    except Exception:
        pass


def render_auth_screen():
    st.markdown("<style>.stApp{background-color:#0B1E1B;}</style>", unsafe_allow_html=True)
    _, center, _ = st.columns([1, 1.4, 1])
    with center:
        st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="text-align:center; margin-bottom:8px;"><img src="data:image/png;base64,{LAB_LOGO_B64}" style="width:120px;"></div>'
            f'<div style="text-align:center; margin-bottom:6px;"><span style="font-size:22px; font-weight:800; color:#fff;">AI Defense Lab</span></div>'
            f'<div style="text-align:center; margin-bottom:4px; font-size:13px; color:#CBD5E1;">Empowering security practitioners to '
            f'<span style="color:#EF4444; font-weight:700;">Break AI</span> &amp; then '
            f'<span style="color:#10B981; font-weight:700;">Defend AI</span>.</div>'
            f'<div style="text-align:center; margin-bottom:24px; color:#94A3B8; font-size:12px;">Build your AI security portfolio. Level by level.</div>',
            unsafe_allow_html=True,
        )
        if st.session_state.auth_error:
            st.error(st.session_state.auth_error)
        if st.session_state.auth_success:
            st.success(st.session_state.auth_success)
        tab_in, tab_up = st.tabs(["Sign In", "Create Account"])
        with tab_in:
            email    = st.text_input("Email", key="si_email", placeholder="you@example.com")
            password = st.text_input("Password", type="password", key="si_pass", placeholder="••••••••")
            st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)
            if st.button("Sign In →", use_container_width=True, key="si_btn"):
                if email and password:
                    do_sign_in(email, password)
                else:
                    st.warning("Enter your email and password.")
        with tab_up:
            full_name = st.text_input("Full Name", key="su_name", placeholder="Your full name")
            email_up  = st.text_input("Email", key="su_email", placeholder="you@example.com")
            pass_up   = st.text_input("Password (min 6 characters)", type="password", key="su_pass")
            st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)
            if st.button("Create Account →", use_container_width=True, key="su_btn"):
                if full_name and email_up and pass_up:
                    do_sign_up(email_up, pass_up, full_name)
                else:
                    st.warning("Fill in all three fields.")
        st.markdown(
            f'<div style="text-align:center; margin-top:16px;">'
            f'<img src="data:image/png;base64,{HN_LOGO_B64}" style="height:28px; opacity:0.7; vertical-align:middle; margin-right:8px;">'
            f'<span style="color:#475569; font-size:11px; vertical-align:middle;">AI Security Fellowship</span>'
            f'</div>',
            unsafe_allow_html=True,
        )


ONBOARDING_STEPS = [
    {
        "title": "Welcome to AI Defense Lab",
        "body_html": (
            '<p style="color:#E2E8F0; font-size:14px; line-height:1.8; margin-bottom:12px;">'
            'This is a free, open-source lab where you practice real AI security defence skills '
            '— not by reading theory, but by working on intentionally vulnerable systems.'
            '</p>'
            '<p style="color:#E2E8F0; font-size:14px; line-height:1.8;">'
            'You will find real vulnerabilities, write real fixes, and commit real code. '
            'By the time you finish, you will have a portfolio a hiring manager can actually examine.'
            '</p>'
        ),
        "emoji": "🛡️",
        "has_name_input": True,
    },
    {
        "title": "How the levels work",
        "body_html": (
            '<p style="color:#E2E8F0; font-size:14px; line-height:1.8; margin-bottom:12px;">'
            'The lab has <strong style="color:#A7F3D0;">5 levels</strong>, each covering a different domain of AI security. '
            'Level 1 starts at the beginning — cloud infrastructure and log forensics. '
            'Each level unlocks only after you complete the one before it.'
            '</p>'
            '<p style="color:#E2E8F0; font-size:14px; line-height:1.8;">'
            'When you fix a vulnerability and commit the code to your GitHub fork, that commit becomes your portfolio evidence. '
            'One fork. One Hugging Face Space. Five clean commits.'
            '</p>'
        ),
        "emoji": "🔓",
        "has_name_input": False,
    },
    {
        "title": "Your portfolio is the point",
        "body_html": (
            '<p style="color:#E2E8F0; font-size:14px; line-height:1.8; margin-bottom:12px;">'
            'Every level ends with a commit to your GitHub fork showing exactly what you changed and why. '
            'A recruiter can click the link and see the before and the after — instantly.'
            '</p>'
            '<p style="color:#E2E8F0; font-size:14px; line-height:1.8;">'
            'Fill in <strong style="color:#A7F3D0;">PORTFOLIO.md</strong> in your repo as you go. '
            'By Level 5, you have five documented defensive skills and a live proof-of-work repo under your own name.'
            '</p>'
        ),
        "emoji": "📁",
        "has_name_input": False,
    },
]


def render_onboarding():
    st.markdown("<style>.stApp{background-color:#0B1E1B;}</style>", unsafe_allow_html=True)
    _, center, _ = st.columns([1, 1.6, 1])
    step = st.session_state.onboarding_step
    data = ONBOARDING_STEPS[step]
    with center:
        st.markdown("<div style='height:60px;'></div>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="background:#112823; border:1px solid #1a3530; border-radius:14px; padding:36px;">'
            f'<div style="font-size:40px; text-align:center; margin-bottom:16px;">{data["emoji"]}</div>'
            f'<div style="font-size:11px; color:#A7F3D0; text-align:center; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:8px;">Step {step+1} of {len(ONBOARDING_STEPS)}</div>'
            f'<div style="font-size:22px; font-weight:800; color:#fff; text-align:center; margin-bottom:20px;">{data["title"]}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown(data["body_html"], unsafe_allow_html=True)

        if data.get("has_name_input"):
            st.markdown('<div style="color:#A7F3D0; font-size:11px; font-weight:700; letter-spacing:1px; text-transform:uppercase; margin-top:16px; margin-bottom:6px;">What should we call you?</div>', unsafe_allow_html=True)
            name_val = st.text_input(
                "full_name",
                value=st.session_state.pending_full_name,
                placeholder="Enter your full name",
                key="onboard_name_input",
                label_visibility="collapsed",
            )
            if name_val:
                st.session_state.pending_full_name = name_val

        dots = "".join(
            f'<span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:{"#10B981" if i == step else "#1a3530"}; margin:0 4px;"></span>'
            for i in range(len(ONBOARDING_STEPS))
        )
        st.markdown(f'<div style="text-align:center; margin:20px 0;">{dots}</div>', unsafe_allow_html=True)
        b1, b2 = st.columns(2)
        with b1:
            if step > 0:
                if st.button("← Back", use_container_width=True):
                    st.session_state.onboarding_step -= 1
                    st.rerun()
        with b2:
            if step < len(ONBOARDING_STEPS) - 1:
                if st.button("Next →", use_container_width=True):
                    if step == 0 and st.session_state.pending_full_name:
                        try:
                            get_authed_client().table("defense_lab_users").update(
                                {"full_name": st.session_state.pending_full_name}
                            ).eq("id", str(st.session_state.user.id)).execute()
                        except Exception:
                            pass
                    st.session_state.onboarding_step += 1
                    st.rerun()
            else:
                if st.button("Enter the Lab →", use_container_width=True):
                    mark_onboarding_complete()
                    st.rerun()


LEVEL_META = [
    {"num": 1, "name": "MedVitals AI",      "sector": "HealthTech", "domain": "Cloud Infrastructure Security", "color": "#10B981"},
    {"num": 2, "name": "DataForge ML",       "sector": "BioTech",    "domain": "AI Model Security",             "color": "#6366F1"},
    {"num": 3, "name": "CartBot AI",         "sector": "E-Commerce", "domain": "Application & API Security",    "color": "#F97316"},
    {"num": 4, "name": "PayGuard",           "sector": "FinTech",    "domain": "Data Security in AI",           "color": "#F59E0B"},
    {"num": 5, "name": "LegalBot Municipal", "sector": "GovTech",    "domain": "Agentic AI Security",           "color": "#EF4444"},
]


def render_hub(profile, progress):
    st.markdown("<style>.stApp{background-color:#0B1E1B;}</style>", unsafe_allow_html=True)
    st.sidebar.markdown(
        f'<div style="text-align:center; margin-bottom:8px;"><img src="data:image/png;base64,{LAB_LOGO_B64}" style="width:90px;"></div>',
        unsafe_allow_html=True,
    )
    display_name = profile.get("full_name") or st.session_state.user.email
    st.sidebar.markdown(f"**{display_name}**")
    st.sidebar.caption(st.session_state.user.email)
    st.sidebar.markdown("---")
    if not profile.get("full_name"):
        new_name = st.sidebar.text_input("Your name:", placeholder="Enter your full name", key="hub_name_input")
        if st.sidebar.button("Save name", key="hub_save_name"):
            if new_name.strip():
                try:
                    get_authed_client().table("defense_lab_users").update(
                        {"full_name": new_name.strip()}
                    ).eq("id", str(st.session_state.user.id)).execute()
                    st.rerun()
                except Exception:
                    pass
        st.sidebar.markdown("---")
    completed_count = sum(1 for p in progress.values() if p.get("completed"))
    st.sidebar.metric("Levels Completed", f"{completed_count} / 5")
    st.sidebar.markdown("---")
    if st.sidebar.button("Sign Out"):
        do_sign_out()

    first = profile.get("full_name", "").split()[0] if profile.get("full_name") else "there"
    st.markdown(
        f'<div style="background:linear-gradient(135deg, #0B7B6E 0%, #0B1E1B 75%); padding:40px 50px; border-radius:14px; margin-bottom:30px;">'
        f'<div style="font-size:28px; font-weight:800; color:#fff;">Welcome back, {first} 👋</div>'
        f'<div style="font-size:13px; color:#CBD5E1; margin-top:8px;">Empowering security practitioners to '
        f'<span style="color:#EF4444; font-weight:700;">Break AI</span> &amp; then '
        f'<span style="color:#A7F3D0; font-weight:700;">Defend AI</span>.</div>'
        f'<div style="margin-top:14px; font-size:13px; color:#A7F3D0;">{completed_count} of 5 levels complete</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
    st.markdown("### Your Lab Progress")

    for meta in LEVEL_META:
        n = meta["num"]
        lp           = progress.get(n, {})
        is_complete  = lp.get("completed", False)
        is_unlocked  = n == 1 or progress.get(n - 1, {}).get("completed", False)
        c            = meta["color"]

        if is_complete:
            badge = f'<span style="background:#10B981; color:#fff; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:700;">✓ COMPLETE</span>'
        elif is_unlocked:
            badge = '<span style="background:#E8A832; color:#1a1a1a; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:700;">IN PROGRESS</span>'
        else:
            badge = '<span style="background:#374151; color:#9CA3AF; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:700;">🔒 LOCKED</span>'

        st.markdown(
            f'<div style="background:#112823; border:1px solid #1a3530; border-radius:10px; padding:18px 24px; margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;"><div><div style="font-size:11px; color:{c}; font-weight:700; text-transform:uppercase; letter-spacing:1px; margin-bottom:4px;">Level {n} · {meta["sector"]}</div><div style="font-size:18px; font-weight:700; color:#fff; margin-bottom:4px;">{meta["name"]}</div><div style="font-size:12px; color:#94A3B8;">{meta["domain"]}</div></div><div style="margin-top:8px;">{badge}</div></div>',
            unsafe_allow_html=True,
        )
        if is_unlocked:
            label = f"Review Level {n}" if is_complete else f"Enter Level {n} →"
            if st.button(label, key=f"hub_btn_{n}"):
                st.session_state.view = f"level{n}"
                st.rerun()


def render_level_view(view_name, profile, progress):
    from levels.level1_medvitals import render_level1
    from levels.level2_dataforge import render_level2
    from levels.level3_cartbot   import render_level3
    from levels.level4_payguard  import render_level4
    from levels.level5_legalbot  import render_level5

    level_map = {
        "level1": (render_level1, 1),
        "level2": (render_level2, 2),
        "level3": (render_level3, 3),
        "level4": (render_level4, 4),
        "level5": (render_level5, 5),
    }
    render_fn, level_num = level_map[view_name]
    is_unlocked = level_num == 1 or progress.get(level_num - 1, {}).get("completed", False)

    st.sidebar.markdown(
        f'<div style="text-align:center; margin-bottom:4px;"><img src="data:image/png;base64,{LAB_LOGO_B64}" style="width:80px;"></div><div style="text-align:center; margin-bottom:2px;"><img src="data:image/png;base64,{HN_LOGO_B64}" style="height:22px; opacity:0.8;"></div><div style="text-align:center; font-size:10px; color:#64748B; letter-spacing:0.5px; margin-bottom:8px;">AI SECURITY FELLOWSHIP</div>',
        unsafe_allow_html=True,
    )
    st.sidebar.markdown(f"**{profile.get('full_name') or st.session_state.user.email}**")
    st.sidebar.caption(st.session_state.user.email)
    st.sidebar.markdown("---")
    if st.sidebar.button("← Back to Hub"):
        st.session_state.view = "hub"
        st.rerun()
    if st.sidebar.button("Sign Out"):
        do_sign_out()

    st.markdown("<style>.stApp{background-color:#ffffff;}</style>", unsafe_allow_html=True)

    bc1, bc2 = st.columns([1, 7])
    with bc1:
        if st.button("⬅ Hub", key=f"bc_{level_num}"):
            st.session_state.view = "hub"
            st.rerun()
    with bc2:
        st.markdown(
            f'<div style="padding-top:6px; color:#64748B; font-size:13px;">'
            f'Level {level_num} &nbsp;/&nbsp; {LEVEL_META[level_num-1]["name"]} &nbsp;·&nbsp; {LEVEL_META[level_num-1]["domain"]}'
            f'</div>',
            unsafe_allow_html=True,
        )

    if not is_unlocked:
        prev = LEVEL_META[level_num - 2]["name"]
        st.error(f"🔒 This level is locked. Complete Level {level_num - 1} — {prev} — first.")
        return

    render_fn(st.session_state.user, get_authed_client())


# ── Main router ────────────────────────────────────────────────────────────────
if st.session_state.user is None:
    render_auth_screen()
else:
    profile  = get_user_profile()
    progress = get_progress()
    if not profile.get("onboarding_complete", False):
        render_onboarding()
    elif st.session_state.view == "hub":
        render_hub(profile, progress)
    elif st.session_state.view.startswith("level"):
        render_level_view(st.session_state.view, profile, progress)
    else:
        st.session_state.view = "hub"
        st.rerun()
