import streamlit as st
import base64
import os

st.set_page_config(
    page_title="AI Security Fellowship — Defense Lab",
    page_icon="🛡️",
    layout="wide",
)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 1rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

PHASE2_TOKEN = "PAYGUARD_SECURE_PHASE2"
PHASE3_TOKEN = "LEGALBOT_CONTAINMENT_PHASE3"
ASSETS_DIR = os.path.dirname(__file__) # Fixed path to search root folder

if "view" not in st.session_state:
    st.session_state.view = "lobby"
if "phase2_unlocked" not in st.session_state:
    st.session_state.phase2_unlocked = False
if "phase3_unlocked" not in st.session_state:
    st.session_state.phase3_unlocked = False


def get_base64_image(filename):
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


LOGO_B64 = get_base64_image("hernetiq_logo.png")

MESH_SVG = """
<svg viewBox="0 0 1000 150" width="100%" height="110" preserveAspectRatio="none">
  <path d="M0,80 C150,20 300,140 500,60 C700,0 850,120 1000,40" fill="none" stroke="#0B7B6E" stroke-width="1.5" opacity="0.5"/>
  <path d="M0,100 C150,40 300,160 500,80 C700,20 850,140 1000,60" fill="none" stroke="#E8A832" stroke-width="1.5" opacity="0.35"/>
  <path d="M0,120 C150,60 300,180 500,100 C700,40 850,160 1000,80" fill="none" stroke="#0B7B6E" stroke-width="1" opacity="0.22"/>
</svg>
"""

ICON_MEDVITALS = """
<svg viewBox="0 0 60 60" width="46" height="46">
  <circle cx="30" cy="30" r="28" fill="#10B981"/>
  <rect x="26" y="14" width="8" height="32" fill="#fff"/>
  <rect x="14" y="26" width="32" height="8" fill="#fff"/>
</svg>
"""

ICON_PAYGUARD = """
<svg viewBox="0 0 60 60" width="46" height="46">
  <circle cx="30" cy="30" r="28" fill="#F59E0B"/>
  <text x="30" y="40" font-size="28" font-weight="bold" fill="#fff" text-anchor="middle" font-family="Arial">$</text>
</svg>
"""

ICON_LEGALBOT = """
<svg viewBox="0 0 60 60" width="46" height="46">
  <circle cx="30" cy="30" r="28" fill="#991B1B"/>
  <line x1="30" y1="14" x2="30" y2="46" stroke="#fff" stroke-width="3"/>
  <line x1="16" y1="22" x2="44" y2="22" stroke="#fff" stroke-width="3"/>
  <circle cx="16" cy="30" r="6" fill="none" stroke="#fff" stroke-width="2"/>
  <circle cx="44" cy="30" r="6" fill="none" stroke="#fff" stroke-width="2"/>
</svg>
"""

ILLUSTRATION_MEDVITALS = """
<svg viewBox="0 0 320 240" width="100%" height="230">
  <circle cx="160" cy="120" r="110" fill="#ECFDF5"/>
  <rect x="90" y="90" width="140" height="110" fill="#0F172A" rx="4"/>
  <polygon points="90,90 160,50 230,90" fill="#10B981"/>
  <rect x="150" y="58" width="20" height="20" fill="#10B981"/>
  <rect x="142" y="66" width="36" height="6" fill="#10B981"/>
  <rect x="110" y="120" width="24" height="24" fill="#fff"/>
  <rect x="146" y="120" width="24" height="24" fill="#fff"/>
  <rect x="182" y="120" width="24" height="24" fill="#fff"/>
  <rect x="110" y="156" width="24" height="24" fill="#fff"/>
  <rect x="146" y="156" width="24" height="24" fill="#fff"/>
  <rect x="182" y="156" width="24" height="24" fill="#fff"/>
  <rect x="148" y="180" width="24" height="20" fill="#94A3B8"/>
  <polyline points="20,210 60,210 75,180 90,230 105,150 120,210 300,210" fill="none" stroke="#10B981" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="245" cy="150" r="12" fill="#F1C9A6"/>
  <rect x="233" y="162" width="24" height="40" rx="6" fill="#0EA5E9"/>
  <circle cx="275" cy="160" r="11" fill="#E8B589"/>
  <rect x="264" y="171" width="22" height="36" rx="6" fill="#CBD5E1"/>
</svg>
"""

ILLUSTRATION_PAYGUARD = """
<svg viewBox="0 0 320 240" width="100%" height="230">
  <circle cx="160" cy="120" r="110" fill="#FFFBEB"/>
  <rect x="70" y="100" width="120" height="80" rx="10" fill="#334155"/>
  <rect x="70" y="100" width="120" height="20" rx="10" fill="#1E293B"/>
  <circle cx="90" cy="110" r="5" fill="#F59E0B"/>
  <rect x="200" y="140" width="20" height="50" fill="#F59E0B"/>
  <rect x="225" y="120" width="20" height="70" fill="#FBBF24"/>
  <rect x="250" y="100" width="20" height="90" fill="#F59E0B"/>
  <circle cx="50" cy="180" r="14" fill="#FBBF24" stroke="#92400E" stroke-width="2"/>
  <circle cx="72" cy="196" r="10" fill="#FBBF24" stroke="#92400E" stroke-width="2"/>
  <circle cx="120" cy="200" r="11" fill="#F1C9A6"/>
  <rect x="109" y="211" width="22" height="26" rx="5" fill="#1E293B"/>
  <circle cx="155" cy="198" r="11" fill="#E8B589"/>
  <rect x="144" y="209" width="22" height="26" rx="5" fill="#475569"/>
  <rect x="128" y="195" width="18" height="14" fill="#fff" stroke="#94A3B8" stroke-width="1"/>
</svg>
"""

ILLUSTRATION_LEGALBOT = """
<svg viewBox="0 0 320 240" width="100%" height="230">
  <circle cx="160" cy="120" r="110" fill="#FEF2F2"/>
  <polygon points="100,90 160,55 220,90" fill="#991B1B"/>
  <rect x="95" y="90" width="130" height="14" fill="#1E1E1E"/>
  <rect x="105" y="104" width="14" height="70" fill="#9CA3AF"/>
  <rect x="130" y="104" width="14" height="70" fill="#9CA3AF"/>
  <rect x="155" y="104" width="14" height="70" fill="#9CA3AF"/>
  <rect x="180" y="104" width="14" height="70" fill="#9CA3AF"/>
  <rect x="205" y="104" width="14" height="70" fill="#9CA3AF"/>
  <rect x="90" y="174" width="140" height="14" fill="#1E1E1E"/>
  <line x1="255" y1="95" x2="255" y2="160" stroke="#991B1B" stroke-width="4"/>
  <line x1="230" y1="112" x2="280" y2="112" stroke="#991B1B" stroke-width="4"/>
  <circle cx="230" cy="128" r="10" fill="none" stroke="#991B1B" stroke-width="3"/>
  <circle cx="280" cy="128" r="10" fill="none" stroke="#991B1B" stroke-width="3"/>
  <rect x="40" y="150" width="40" height="50" fill="#fff" stroke="#991B1B" stroke-width="2"/>
  <line x1="48" y1="162" x2="72" y2="162" stroke="#991B1B" stroke-width="2"/>
  <line x1="48" y1="172" x2="72" y2="172" stroke="#991B1B" stroke-width="2"/>
  <line x1="48" y1="182" x2="62" y2="182" stroke="#991B1B" stroke-width="2"/>
</svg>
"""


def set_background(color, text_color):
    st.markdown(
        f"<style>.stApp {{ background-color: {color}; color: {text_color}; }}</style>",
        unsafe_allow_html=True,
    )


def hero_header_bar(gradient_css, company_name, nav_left, nav_right):
    st.markdown(
        f"""
        <div style="background:{gradient_css}; padding:18px 32px; border-radius:8px;
                    display:flex; justify-content:space-between; align-items:center; margin-bottom:28px;">
          <div style="color:#fff; font-size:22px; font-weight:700;">{company_name}</div>
          <div style="color:#E5E7EB; font-size:13px;">{nav_left}&nbsp;&nbsp;&nbsp;&nbsp;{nav_right}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def decorative_buttons(primary_label, secondary_label, accent_color):
    st.markdown(
        f"""
        <div style="margin-top:18px;">
          <span style="background:{accent_color}; color:#1a1a1a; padding:10px 22px;
                      border-radius:6px; font-weight:600; font-size:14px; margin-right:12px;
                      display:inline-block;">{primary_label}</span>
          <span style="border:1px solid #94A3B8; color:inherit; padding:10px 22px;
                      border-radius:6px; font-weight:500; font-size:14px;
                      display:inline-block;">{secondary_label}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def sidebar():
    st.sidebar.markdown(
        f"""
        <div style="text-align:center; margin-bottom:8px;">
          <img src="data:image/png;base64,{LOGO_B64}" style="max-width:170px;">
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.caption("AI Security Fellowship — Defense Lab")
    st.sidebar.markdown("---")

    student_id = st.sidebar.text_input(
        "Enter Your Student ID (Full Name or Email)",
        value="STUDENT_ID_PLACEHOLDER",
        help="Replace this on Day 1 with your real name or email. This stamps every log and screenshot so your work can't be confused with a classmate's.",
    )

    st.sidebar.markdown("---")

    if st.session_state.view != "lobby":
        if st.sidebar.button("← Back to Lobby"):
            st.session_state.view = "lobby"
            st.rerun()

    st.sidebar.caption(f"Active Student: **{student_id}**")
    return student_id


def render_lobby(student_id):
    set_background("#0B1E1B", "#F1F5F9")

    st.markdown(
        f"""
        <div style="background:linear-gradient(135deg, #0B7B6E 0%, #0B1E1B 75%);
                    padding:50px 50px 30px 50px; border-radius:14px; position:relative; overflow:hidden;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
            <div style="max-width:560px;">
              <div style="font-size:38px; font-weight:800; line-height:1.25; color:#fff;">
                AI security for blue teams.<br>Get your hands dirty, not lectured.
              </div>
              <div style="font-size:15px; color:#CBD5E1; margin-top:14px;">
                A live, multi-sector defense lab built for the AI Security Fellowship.
              </div>
              <div style="margin-top:10px; font-size:13px; color:#A7F3D0;">
                ✓ Real startup architectures &nbsp;&nbsp; ✓ Live vulnerability simulations
              </div>
            <div style="background:#fff; border-radius:16px; padding:18px 26px;
                        box-shadow:0 8px 24px rgba(0,0,0,0.3); margin-top:10px;">
              <img src="data:image/png;base64,{LOGO_B64}" style="max-width:170px; display:block;">
          </div> 
          
          <div style="margin-top:10px;">
            {MESH_SVG}
          </div>

          <div style="margin-top:18px;">
              <span style="background:#E8A832;color:#1a1a1a;padding:10px 22px;
                  border-radius:6px;font-weight:600;font-size:14px;
                  margin-right:12px;display:inline-block;">
                  Enter the Lab
              </span>

              <span style="border:1px solid #94A3B8;color:white;
                  padding:10px 22px;border-radius:6px;
                  font-weight:500;font-size:14px;
                  display:inline-block;">
                  View the Syllabus
              </span>
          </div>
          
         </div>
         </div>
         </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Select Active Target Environment")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(ICON_MEDVITALS, unsafe_allow_html=True)
        st.markdown("**MedVitals AI**")
        st.caption("HealthTech — AI triage portal")
        st.markdown(
            "<span style='background:#10B981; color:#04221A; padding:3px 10px; "
            "border-radius:12px; font-size:11px; font-weight:600;'>UNLOCKED</span>",
            unsafe_allow_html=True,
        )
        if st.button("Enter MedVitals AI", key="enter_mv"):
            st.session_state.view = "medvitals"
            st.rerun()

    with col2:
        st.markdown(ICON_PAYGUARD, unsafe_allow_html=True)
        st.markdown("**PayGuard FinTech**")
        st.caption("FinTech — Multi-tenant wallet")
        badge = "UNLOCKED" if st.session_state.phase2_unlocked else "LOCKED"
        badge_color = "#10B981" if st.session_state.phase2_unlocked else "#7F1D1D"
        text_color = "#04221A" if st.session_state.phase2_unlocked else "#FCA5A5"
        st.markdown(
            f"<span style='background:{badge_color}; color:{text_color}; padding:3px 10px; "
            f"border-radius:12px; font-size:11px; font-weight:600;'>{badge}</span>",
            unsafe_allow_html=True,
        )
        if st.button("Enter PayGuard FinTech", key="enter_pg"):
            st.session_state.view = "payguard"
            st.rerun()

    with col3:
        st.markdown(ICON_LEGALBOT, unsafe_allow_html=True)
        st.markdown("**LegalBot GovTech**")
        st.caption("GovTech — Autonomous legal agent")
        badge = "UNLOCKED" if st.session_state.phase3_unlocked else "LOCKED"
        badge_color = "#10B981" if st.session_state.phase3_unlocked else "#7F1D1D"
        text_color = "#04221A" if st.session_state.phase3_unlocked else "#FCA5A5"
        st.markdown(
            f"<span style='background:{badge_color}; color:{text_color}; padding:3px 10px; "
            f"border-radius:12px; font-size:11px; font-weight:600;'>{badge}</span>",
            unsafe_allow_html=True,
        )
        if st.button("Enter LegalBot GovTech", key="enter_lb"):
            st.session_state.view = "legalbot"
            st.rerun()


def render_medvitals(student_id):
    set_background("#FFFFFF", "#0F172A")
    hero_header_bar(
        "linear-gradient(135deg, #0F172A 0%, #1E293B 100%)",
        "MedVitals AI",
        "Patient Login",
        "Provider Access",
    )

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(
            """
            <div style="font-size:32px; font-weight:800; color:#0F172A; line-height:1.3;">
              Healthcare, connected<br>and compromised.
            </div>
            <div style="font-size:14px; color:#475569; margin-top:12px; max-width:420px;">
              An intentionally vulnerable AI triage platform, built so blue
              teams can practice finding and fixing real clinical data flaws.
            </div>
            """,
            unsafe_allow_html=True,
        )
        decorative_buttons("Access Portal", "Learn More", "#10B981")
    with col2:
        st.markdown(ILLUSTRATION_MEDVITALS, unsafe_allow_html=True)

    st.markdown("---")

    lab_col1, lab_col2 = st.columns([2, 1])
    with lab_col1:
        st.markdown("#### AI Triage Chat")
        st.text_area("Patient message to AI Triage Nurse:", placeholder="Describe your symptoms...")
        if st.button("Send to Triage AI"):
            st.success(
                "🩺 AI Triage Nurse: Thank you. Based on your symptoms, please monitor your condition "
                "and seek in-person care if symptoms worsen within 24 hours."
            )
    with lab_col2:
        st.markdown("#### Vitals Ticker")
        st.metric("Heart Rate", "72 BPM", "Stable")
        st.metric("Blood Oxygen", "98%", "Normal")
        st.metric("Patients Active", "1,204", "+12 today")

    st.markdown("---")
    st.markdown("#### ⚠️ Admin Console — Deployment Configuration")
    st.code(
        '# config.py — production deployment wrapper\n'
        'AWS_SECRET_ACCESS_KEY = "AKIA-VULNERABLE-MOCK-CREDENTIAL-998877"\n'
        'AWS_REGION = "us-east-1"\n'
        'DB_CONNECTION_STRING = "postgresql://admin:[email protected]:5432/medvitals_prod"',
        language="python",
    )
    st.caption("This key is hardcoded directly in the client-facing deployment wrapper.")

    st.markdown("#### AWS CloudTrail Raw Log Dump")
    cloudtrail_logs = [
        {"EventTime": "2026-06-30T02:14:11Z", "EventName": "ConsoleLogin", "SourceIPAddress": "10.0.4.22",
         "UserAgent": "Mozilla/5.0", "UserIdentity": "medvitals-deploy-bot", "StudentID": student_id},
        {"EventTime": "2026-06-30T02:14:45Z", "EventName": "DescribeInstances", "SourceIPAddress": "10.0.4.22",
         "UserAgent": "aws-cli/2.13", "UserIdentity": "medvitals-deploy-bot", "StudentID": student_id},
        {"EventTime": "2026-06-30T03:02:09Z", "EventName": "AssumeRole", "SourceIPAddress": "198.51.100.45",
         "UserAgent": "python-requests/2.28.1", "UserIdentity": "medvitals-deploy-bot",
         "RequestParameters": {"roleArn": "arn:aws:iam::000000000000:role/AdminFullAccess"}, "StudentID": student_id},
        {"EventTime": "2026-06-30T03:02:31Z", "EventName": "ListBuckets", "SourceIPAddress": "198.51.100.45",
         "UserAgent": "python-requests/2.28.1", "UserIdentity": "medvitals-deploy-bot", "StudentID": student_id},
        {"EventTime": "2026-06-30T03:03:02Z", "EventName": "PutObject", "SourceIPAddress": "198.51.100.45",
         "UserAgent": "python-requests/2.28.1", "UserIdentity": "medvitals-deploy-bot",
         "RequestParameters": {"bucketName": "medvitals-patient-records", "status": "Success (Privilege Escalation Vector)"}, "StudentID": student_id},
    ]
    st.json(cloudtrail_logs)
    st.caption("Task: Identify the indicator of compromise (IoC) in this log set and write your Incident Timeline Report.")


def render_payguard(student_id, unlocked):
    set_background("#FFFFFF", "#0F172A")
    hero_header_bar(
        "linear-gradient(135deg, #334155 0%, #1E293B 100%)",
        "PayGuard Wallet",
        "Business Login",
        "Partner Access",
    )

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(
            """
            <div style="font-size:32px; font-weight:800; color:#0F172A; line-height:1.3;">
              Payments, fast<br>and unguarded.
            </div>
            <div style="font-size:14px; color:#475569; margin-top:12px; max-width:420px;">
              An intentionally vulnerable multi-tenant fintech wallet platform,
              built to simulate the data isolation flaws found in fast-shipped AI SaaS products.
            </div>
            """,
            unsafe_allow_html=True,
        )
        decorative_buttons("Access Portal", "Learn More", "#F59E0B")
    with col2:
        st.markdown(ILLUSTRATION_PAYGUARD, unsafe_allow_html=True)

    st.markdown("---")

    if not unlocked:
        render_lock_screen(
            "🔒 PAYGUARD FINTECH IS LOCKED. Complete Month 1, analyze your AWS CloudTrail logs, "
            "and enter your verified Phase 2 Access Token to proceed.",
            PHASE2_TOKEN,
            "phase2_unlocked",
        )
        return

    tenant_ledger = {
        "Tenant_A_Fintech": {"balance": 450000, "account_owner": "Quanta Capital Partners"},
        "Tenant_B_Retail": {"balance": 1200000, "account_owner": "Brightline Retail Holdings"},
    }

    lab_col1, lab_col2 = st.columns(2)
    with lab_col1:
        st.markdown("#### Wallet Ledger")
        for tenant, data in tenant_ledger.items():
            st.metric(tenant, f"${data['balance']:,}", data["account_owner"])
    with lab_col2:
        st.markdown("#### Invoice Ingestion Portal")
        uploaded_invoice = st.file_uploader("Upload Invoice (PDF or TXT)", type=["pdf", "txt"])
        if uploaded_invoice:
            st.info("Invoice received. Extracting embedded text and forwarding to vector context window...")

    st.markdown("---")
    st.markdown("#### Automated Loan Approver Assistant (RAG Chat)")
    active_session = st.selectbox("Active Tenant Session", list(tenant_ledger.keys()))
    chat_input = st.text_input("Ask the AI Transaction Risk Auditor:", placeholder="e.g. What is my current balance?")

    if st.button("Submit Query"):
        if "INJECT_SYSTEM_CONTEXT_OVERRIDE" in chat_input.upper():
            st.error("⚠️ CROSS-TENANT CONTEXT LEAK DETECTED")
            st.json(
                {
                    "active_session": active_session,
                    "leaked_context": tenant_ledger,
                    "vulnerability": (
                        "No tenant_id boundary check was applied. The retrieval function pulled the "
                        "FULL ledger dictionary into the active session's context window."
                    ),
                    "StudentID": student_id,
                }
            )
        else:
            st.success(f"🤖 AI Auditor: Your current balance for {active_session} is ${tenant_ledger[active_session]['balance']:,}.")

    st.caption("Task: Build a metadata filtering routine (tenant_id == active_session_id) that prevents this cross-tenant context leak.")


def render_legalbot(student_id, unlocked):
    set_background("#FFFFFF", "#0F172A")
    hero_header_bar(
        "linear-gradient(135deg, #1E1E1E 0%, #3F1212 100%)",
        "LegalBot Municipal",
        "Citizen Portal",
        "Staff Login",
    )

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(
            """
            <div style="font-size:32px; font-weight:800; color:#0F172A; line-height:1.3;">
              Municipal operations,<br>automated and unchecked.
            </div>
            <div style="font-size:14px; color:#475569; margin-top:12px; max-width:420px;">
              An intentionally vulnerable autonomous legal agent platform, built to
              simulate excessive agency risk in municipal tool-calling systems.
            </div>
            """,
            unsafe_allow_html=True,
        )
        decorative_buttons("Access Portal", "Learn More", "#991B1B")
    with col2:
        st.markdown(ILLUSTRATION_LEGALBOT, unsafe_allow_html=True)

    st.markdown("---")

    if not unlocked:
        render_lock_screen(
            "🔒 LEGALBOT GOVTECH IS LOCKED. Complete Month 2, fix the FinTech RAG boundaries, "
            "and enter your Phase 3 Access Token.",
            PHASE3_TOKEN,
            "phase3_unlocked",
        )
        return

    st.markdown("#### Contract Markdown Scanner")
    st.file_uploader("Upload Contract Text (MD or TXT)", type=["md", "txt"])

    st.markdown("#### Municipal Case Registry")
    case_registry = [
        {"case_id": "2026-GA-091", "title": "Contract Review — Sanitation Dept Vendor", "status": "Open"},
        {"case_id": "2026-GA-104", "title": "Zoning Dispute — Riverside Parcel", "status": "Pending"},
        {"case_id": "2026-GA-118", "title": "Procurement Audit — Fleet Services", "status": "Open"},
    ]
    st.table(case_registry)

    st.markdown("---")
    st.markdown("#### Autonomous Legal Agent Process Manager")
    agent_command = st.text_area("Send instruction to the Autonomous Legal Agent:", placeholder="e.g. Pull case 2026-GA-091 status")

    def trigger_municipal_tool(action_parameter):
        if "DROP_TABLE" in action_parameter.upper() or "PURGE" in action_parameter.upper():
            return "CRITICAL_FAILURE"
        return "OK"

    if st.button("Execute Automated Legal Dispatch Tool"):
        result = trigger_municipal_tool(agent_command)
        if result == "CRITICAL_FAILURE":
            st.markdown(
                "<div style='background-color:#000000; color:#FF0000; padding:15px; "
                "font-family:monospace; border:1px solid #991B1B;'>"
                "[CRITICAL EXECUTION ERROR: SYSTEM TABLE PURGED]<br>"
                "[trace] core_case_scheduling_tables → DROPPED<br>"
                f"[session] StudentID: {student_id}<br>"
                "[cause] Unvalidated tool parameter executed with native OS-level privileges."
                "</div>",
                unsafe_allow_html=True,
            )
        else:
            st.success(f"🤖 LegalBot Agent: Processing instruction — '{agent_command}'. Dispatch logged.")

    st.caption("Task: Write an Input/Output Schema Validator that rejects non-standard parameters before they reach trigger_municipal_tool().")


def render_lock_screen(message, token_constant, session_key):
    st.error(message)
    token_input = st.text_input("Access Token", type="password", key=f"{session_key}_input")
    if st.button("Unlock", key=f"{session_key}_button"):
        if token_input == token_constant:
            st.session_state[session_key] = True
            st.rerun()
        else:
            st.warning("Incorrect token. Verify your previous submission with your instructor.")


student_id = sidebar()

if st.session_state.view == "lobby":
    render_lobby(student_id)
elif st.session_state.view == "medvitals":
    render_medvitals(student_id)
elif st.session_state.view == "payguard":
    render_payguard(student_id, st.session_state.phase2_unlocked)
elif st.session_state.view == "legalbot":
    render_legalbot(student_id, st.session_state.phase3_unlocked)
