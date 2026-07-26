import streamlit as st

ILLUSTRATION_MEDVITALS = '<svg viewBox="0 0 320 240" width="100%" height="220"><circle cx="160" cy="120" r="110" fill="#ECFDF5"/><rect x="90" y="90" width="140" height="110" fill="#0F172A" rx="4"/><polygon points="90,90 160,50 230,90" fill="#10B981"/><rect x="150" y="58" width="20" height="20" fill="#10B981"/><rect x="142" y="66" width="36" height="6" fill="#10B981"/><rect x="110" y="120" width="24" height="24" fill="#fff"/><rect x="146" y="120" width="24" height="24" fill="#fff"/><rect x="182" y="120" width="24" height="24" fill="#fff"/><rect x="110" y="156" width="24" height="24" fill="#fff"/><rect x="146" y="156" width="24" height="24" fill="#fff"/><rect x="182" y="156" width="24" height="24" fill="#fff"/><rect x="148" y="180" width="24" height="20" fill="#94A3B8"/><polyline points="20,210 60,210 75,180 90,230 105,150 120,210 300,210" fill="none" stroke="#10B981" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="245" cy="150" r="12" fill="#F1C9A6"/><rect x="233" y="162" width="24" height="40" rx="6" fill="#0EA5E9"/><circle cx="275" cy="160" r="11" fill="#E8B589"/><rect x="264" y="171" width="22" height="36" rx="6" fill="#CBD5E1"/></svg>'

# 16 realistic CloudTrail log entries — no highlighting, no hints
# Students must scan and identify the IoC themselves
CLOUDTRAIL_LOGS = [
    {"event_time": "2026-06-29 23:01:44 UTC", "event_name": "GetObject",             "source_ip": "10.0.4.22",      "user_agent": "aws-sdk-java/1.11.0",     "identity": "medvitals-app-prod"},
    {"event_time": "2026-06-29 23:14:09 UTC", "event_name": "DescribeSecurityGroups","source_ip": "10.0.4.22",      "user_agent": "aws-cli/2.13.0",          "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-29 23:47:33 UTC", "event_name": "GetBucketPolicy",        "source_ip": "10.0.4.22",      "user_agent": "aws-sdk-python/1.26.0",   "identity": "medvitals-app-prod"},
    {"event_time": "2026-06-30 00:12:55 UTC", "event_name": "PutBucketLogging",       "source_ip": "10.0.4.22",      "user_agent": "aws-cli/2.13.0",          "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 00:51:17 UTC", "event_name": "DescribeInstances",      "source_ip": "10.0.4.22",      "user_agent": "aws-cli/2.13.0",          "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 01:03:28 UTC", "event_name": "GetObject",              "source_ip": "10.0.4.22",      "user_agent": "aws-sdk-java/1.11.0",     "identity": "medvitals-app-prod"},
    {"event_time": "2026-06-30 01:22:41 UTC", "event_name": "CreateLogGroup",         "source_ip": "10.0.4.22",      "user_agent": "aws-cli/2.13.0",          "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 01:58:03 UTC", "event_name": "DescribeLogStreams",      "source_ip": "10.0.4.22",      "user_agent": "aws-sdk-python/1.26.0",   "identity": "medvitals-app-prod"},
    {"event_time": "2026-06-30 02:05:19 UTC", "event_name": "ListRoles",              "source_ip": "10.0.4.22",      "user_agent": "aws-cli/2.13.0",          "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 02:14:11 UTC", "event_name": "ConsoleLogin",           "source_ip": "10.0.4.22",      "user_agent": "Mozilla/5.0 (Windows)",   "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 02:14:45 UTC", "event_name": "DescribeInstances",      "source_ip": "10.0.4.22",      "user_agent": "aws-cli/2.13.0",          "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 02:38:04 UTC", "event_name": "GetBucketAcl",           "source_ip": "10.0.4.22",      "user_agent": "aws-sdk-python/1.26.0",   "identity": "medvitals-app-prod"},
    {"event_time": "2026-06-30 02:55:33 UTC", "event_name": "UpdateFunctionCode",     "source_ip": "10.0.4.22",      "user_agent": "aws-cli/2.13.0",          "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 03:02:09 UTC", "event_name": "AssumeRole",             "source_ip": "198.51.100.45",  "user_agent": "python-requests/2.28.1",  "identity": "medvitals-deploy-bot → arn:aws:iam::000000000000:role/AdminFullAccess"},
    {"event_time": "2026-06-30 03:02:31 UTC", "event_name": "ListBuckets",            "source_ip": "198.51.100.45",  "user_agent": "python-requests/2.28.1",  "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 03:03:02 UTC", "event_name": "PutObject",              "source_ip": "198.51.100.45",  "user_agent": "python-requests/2.28.1",  "identity": "medvitals-deploy-bot"},
    {"event_time": "2026-06-30 03:04:18 UTC", "event_name": "GetObject",              "source_ip": "198.51.100.45",  "user_agent": "python-requests/2.28.1",  "identity": "medvitals-deploy-bot"},
]


def render_cloudtrail_table(student_email):
    header = (
        '<div style="background:#0D1117; border:1px solid #30363D; border-radius:8px; overflow:hidden; margin-top:16px;">'
        '<div style="background:#161B22; padding:12px 20px; border-bottom:1px solid #30363D; display:flex; justify-content:space-between; align-items:center;">'
        '<div style="color:#58A6FF; font-weight:600; font-size:14px;">CloudTrail — Event History</div>'
        '<div style="color:#8B949E; font-size:12px;">Filter: Last 24 hours &nbsp;·&nbsp; Region: us-east-1</div>'
        '</div>'
        '<table style="width:100%; border-collapse:collapse; font-family:monospace; font-size:12px;">'
        '<thead>'
        '<tr style="background:#161B22; color:#8B949E; font-size:11px; text-transform:uppercase; letter-spacing:0.5px;">'
        '<th style="padding:10px 16px; text-align:left; border-bottom:1px solid #30363D;">Event Time</th>'
        '<th style="padding:10px 16px; text-align:left; border-bottom:1px solid #30363D;">Event Name</th>'
        '<th style="padding:10px 16px; text-align:left; border-bottom:1px solid #30363D;">Source IP</th>'
        '<th style="padding:10px 16px; text-align:left; border-bottom:1px solid #30363D;">User Agent</th>'
        '<th style="padding:10px 16px; text-align:left; border-bottom:1px solid #30363D;">Identity / Resource</th>'
        '</tr>'
        '</thead>'
        '<tbody>'
    )

    rows = ""
    for log in CLOUDTRAIL_LOGS:
        rows += (
            f'<tr style="border-bottom:1px solid #21262D;">'
            f'<td style="padding:10px 16px; color:#8B949E;">{log["event_time"]}</td>'
            f'<td style="padding:10px 16px; color:#58A6FF;">{log["event_name"]}</td>'
            f'<td style="padding:10px 16px; color:#E6EDF3;">{log["source_ip"]}</td>'
            f'<td style="padding:10px 16px; color:#8B949E;">{log["user_agent"]}</td>'
            f'<td style="padding:10px 16px; color:#E6EDF3; max-width:280px; word-break:break-all;">{log["identity"]}</td>'
            f'</tr>'
        )

    footer = (
        f'<tr><td colspan="5" style="padding:8px 16px; color:#8B949E; font-size:11px; '
        f'background:#161B22; border-top:1px solid #30363D;">Showing {len(CLOUDTRAIL_LOGS)} events '
        f'· Student: {student_email}</td></tr>'
        '</tbody></table></div>'
    )

    st.markdown(header + rows + footer, unsafe_allow_html=True)


def render_level1(user, supabase_client):

    # Check if already completed in Supabase
    if not st.session_state.get("l1_completed"):
        try:
            result = supabase_client.table("defense_lab_progress").select("completed").eq(
                "user_id", str(user.id)
            ).eq("level_number", 1).execute()
            if result.data and result.data[0].get("completed"):
                st.session_state.l1_completed = True
        except Exception:
            pass

    # Domain header
    st.markdown(
        '<div style="background:linear-gradient(135deg, #0B7B6E, #064E3B); border-radius:10px; padding:20px 28px; margin-bottom:24px;">'
        '<div style="color:#A7F3D0; font-size:11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:6px;">Level 1 · Cloud Infrastructure Security</div>'
        '<div style="color:#fff; font-size:15px; margin-bottom:10px;"><strong>Guiding Question:</strong> How do attackers get into AI systems through infrastructure — and how do defenders trace and stop them?</div>'
        '<div style="display:flex; gap:24px; flex-wrap:wrap; margin-top:12px;">'
        '<div><div style="color:#A7F3D0; font-size:11px; font-weight:600; margin-bottom:4px;">HEADLINE TOOLS</div>'
        '<div style="color:#fff; font-size:13px;">AWS CloudTrail · Python-dotenv · IAM Policy Analyzer · GitHub</div></div>'
        '<div><div style="color:#A7F3D0; font-size:11px; font-weight:600; margin-bottom:4px;">ROLES UNLOCKED</div>'
        '<div style="color:#fff; font-size:13px;">Junior Cloud Security Engineer · SOC Analyst Tier 1 · Junior DevSecOps</div></div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    # Hero header
    st.markdown(
        '<div style="background:linear-gradient(135deg, #0F172A 0%, #1E293B 100%); padding:18px 32px; border-radius:8px; display:flex; justify-content:space-between; align-items:center; margin-bottom:28px;">'
        '<div style="color:#fff; font-size:22px; font-weight:700;">MedVitals AI</div>'
        '<div style="color:#E5E7EB; font-size:13px;">Patient Login &nbsp;&nbsp;&nbsp;&nbsp; Provider Access</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(
            '<div style="font-size:32px; font-weight:800; color:#0F172A; line-height:1.3;">Healthcare, connected<br>and compromised.</div>'
            '<div style="font-size:14px; color:#475569; margin-top:12px; max-width:420px;">An intentionally vulnerable AI triage platform. Your job is to find the breach, trace it in the logs, and harden the infrastructure before the next attack.</div>'
            '<div style="margin-top:18px;">'
            '<span style="background:#10B981; color:#fff; padding:10px 22px; border-radius:6px; font-weight:600; font-size:14px; margin-right:12px; display:inline-block;">Begin Audit</span>'
            '<span style="border:1px solid #94A3B8; color:#475569; padding:10px 22px; border-radius:6px; font-weight:500; font-size:14px; display:inline-block;">View Brief</span>'
            '</div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(ILLUSTRATION_MEDVITALS, unsafe_allow_html=True)

    st.markdown("---")

    # Vitals ticker
    v1, v2, v3 = st.columns(3)
    v1.metric("Heart Rate", "72 BPM", "Stable")
    v2.metric("Blood Oxygen", "98%", "Normal")
    v3.metric("Patients Active", "1,204", "+12 today")

    st.markdown("---")

    # Deployment files — no hints, no labels, looks like real repo files
    st.markdown("#### Deployment Repository")
    st.caption("The following files were found in the MedVitals AI GitHub repository.")

    tab1, tab2 = st.tabs(["config.py", "deploy-role-policy.json"])
    with tab1:
        st.code(
            '# config.py\n'
            '# MedVitals AI — Production Environment Configuration\n'
            '# Maintained by: engineering-team@medvitals.ai\n'
            '# Last updated: 2026-05-14\n\n'
            'import os\n\n'
            'APP_ENV = "production"\n'
            'APP_NAME = "medvitals-ai"\n'
            'APP_PORT = 8080\n'
            'LOG_LEVEL = "INFO"\n\n'
            'AWS_SECRET_ACCESS_KEY = "AKIA-MOCK-CREDENTIAL-998877"\n'
            'AWS_REGION = "us-east-1"\n'
            'AWS_ACCOUNT_ID = "000000000000"\n\n'
            'DB_HOST = "medvitals-prod.us-east-1.rds.amazonaws.com"\n'
            'DB_PORT = 5432\n'
            'DB_NAME = "medvitals_prod"\n'
            'DB_USER = "admin"\n'
            'DB_PASSWORD = "Mv@2026!Prod#DB"\n\n'
            'LLM_ENDPOINT = "https://api.openai.com/v1/chat/completions"\n'
            'LLM_MODEL = "gpt-4o"\n'
            'LLM_TIMEOUT = 30\n\n'
            'SESSION_SECRET = "mv-session-k3y-2026-prod"',
            language="python",
        )
    with tab2:
        st.code(
            '{\n'
            '  "Version": "2012-10-17",\n'
            '  "Statement": [\n'
            '    {\n'
            '      "Sid": "MedVitalsServiceRole",\n'
            '      "Effect": "Allow",\n'
            '      "Action": "*",\n'
            '      "Resource": "*"\n'
            '    }\n'
            '  ]\n'
            '}',
            language="json",
        )

    st.markdown("---")

    # CloudTrail — no hints, full 17 entries, students find IoC themselves
    st.markdown("#### AWS CloudTrail — Event History")
    st.caption("A breach occurred last night. Parse the logs below, identify the indicator of compromise (IoC), and write your Incident Timeline Report.")
    render_cloudtrail_table(user.email)

    st.markdown("---")

    # Interview questions
    with st.expander("📋 Interview Questions for This Level"):
        st.markdown(
            "1. Walk me through how you would investigate a suspected cloud credential compromise.\n"
            "2. What is the principle of least privilege and how would you apply it to an IAM policy?\n"
            "3. What CloudTrail fields tell you an AssumeRole attack has occurred?\n"
            "4. What is the difference between hardcoding an API key and using os.environ.get()?"
        )

    st.markdown("---")

    # Submit section
    st.markdown("#### Submit Your Level 1 Work")

    if st.session_state.get("l1_completed"):
        st.success("✅ Level 1 is complete. Level 2 — DataForge ML is now unlocked.")
        if st.button("← Return to Hub", key="l1_return_done"):
            st.session_state.view = "hub"
            st.rerun()
        return

    st.info(
        "Before submitting, confirm you have completed all three tasks:\n\n"
        "1. **Identified the IoC** in the CloudTrail logs and written your Incident Timeline Report.\n"
        "2. **Fixed the credential exposure** — moved secrets out of config.py into environment variables.\n"
        "3. **Rewritten the IAM policy** to enforce Principle of Least Privilege."
    )

    commit_url = st.text_input(
        "GitHub commit URL showing your code fix:",
        placeholder="https://github.com/your-username/ai-security-defense-lab/commit/abc123",
        key="l1_commit_url",
    )
    report_url = st.text_input(
        "Incident Timeline Report link (GitHub Gist, Google Doc, or Medium post):",
        placeholder="https://gist.github.com/your-username/...",
        key="l1_report_url",
    )

    if st.button("Submit Level 1 Work →", key="l1_submit"):
        if not commit_url or not report_url:
            st.warning("Paste both links above before submitting.")
        elif "github.com" not in commit_url and "gitlab.com" not in commit_url:
            st.warning("The first link must be a GitHub or GitLab commit URL.")
        else:
            try:
                supabase_client.table("defense_lab_progress").update({
                    "completed": True,
                    "completed_at": "now()",
                }).eq("user_id", str(user.id)).eq("level_number", 1).execute()
                st.session_state.l1_completed = True
                st.rerun()
            except Exception as e:
                st.error(f"Could not save progress: {e}")
