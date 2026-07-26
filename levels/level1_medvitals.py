import streamlit as st

ILLUSTRATION_MEDVITALS = '<svg viewBox="0 0 320 240" width="100%" height="220"><circle cx="160" cy="120" r="110" fill="#ECFDF5"/><rect x="90" y="90" width="140" height="110" fill="#0F172A" rx="4"/><polygon points="90,90 160,50 230,90" fill="#10B981"/><rect x="150" y="58" width="20" height="20" fill="#10B981"/><rect x="142" y="66" width="36" height="6" fill="#10B981"/><rect x="110" y="120" width="24" height="24" fill="#fff"/><rect x="146" y="120" width="24" height="24" fill="#fff"/><rect x="182" y="120" width="24" height="24" fill="#fff"/><rect x="110" y="156" width="24" height="24" fill="#fff"/><rect x="146" y="156" width="24" height="24" fill="#fff"/><rect x="182" y="156" width="24" height="24" fill="#fff"/><rect x="148" y="180" width="24" height="20" fill="#94A3B8"/><polyline points="20,210 60,210 75,180 90,230 105,150 120,210 300,210" fill="none" stroke="#10B981" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="245" cy="150" r="12" fill="#F1C9A6"/><rect x="233" y="162" width="24" height="40" rx="6" fill="#0EA5E9"/><circle cx="275" cy="160" r="11" fill="#E8B589"/><rect x="264" y="171" width="22" height="36" rx="6" fill="#CBD5E1"/></svg>'

CLOUDTRAIL_LOGS = [
    {
        "event_time": "2026-06-30 02:14:11 UTC",
        "event_name": "ConsoleLogin",
        "source_ip": "10.0.4.22",
        "user_agent": "Mozilla/5.0",
        "identity": "medvitals-deploy-bot",
        "anomaly": False,
    },
    {
        "event_time": "2026-06-30 02:14:45 UTC",
        "event_name": "DescribeInstances",
        "source_ip": "10.0.4.22",
        "user_agent": "aws-cli/2.13",
        "identity": "medvitals-deploy-bot",
        "anomaly": False,
    },
    {
        "event_time": "2026-06-30 03:02:09 UTC",
        "event_name": "AssumeRole",
        "source_ip": "198.51.100.45",
        "user_agent": "python-requests/2.28.1",
        "identity": "medvitals-deploy-bot → AdminFullAccess",
        "anomaly": True,
    },
    {
        "event_time": "2026-06-30 03:02:31 UTC",
        "event_name": "ListBuckets",
        "source_ip": "198.51.100.45",
        "user_agent": "python-requests/2.28.1",
        "identity": "medvitals-deploy-bot",
        "anomaly": True,
    },
    {
        "event_time": "2026-06-30 03:03:02 UTC",
        "event_name": "PutObject",
        "source_ip": "198.51.100.45",
        "user_agent": "python-requests/2.28.1",
        "identity": "medvitals-deploy-bot",
        "anomaly": True,
    },
]


def render_cloudtrail_table(student_email):
    st.markdown(
        '<div style="background:#0D1117; border:1px solid #21262D; border-radius:8px; overflow:hidden; margin-top:16px;">'
        '<div style="background:#161B22; padding:12px 20px; border-bottom:1px solid #21262D; display:flex; justify-content:space-between; align-items:center;">'
        '<div style="color:#58A6FF; font-weight:600; font-size:14px;">CloudTrail — Event History</div>'
        '<div style="color:#8B949E; font-size:12px;">Filter: Last 24 hours · Region: us-east-1</div>'
        '</div>'
        '<table style="width:100%; border-collapse:collapse; font-family:monospace; font-size:12px;">'
        '<thead>'
        '<tr style="background:#161B22; color:#8B949E; font-size:11px; text-transform:uppercase; letter-spacing:0.5px;">'
        '<th style="padding:10px 16px; text-align:left; border-bottom:1px solid #21262D;">Event Time</th>'
        '<th style="padding:10px 16px; text-align:left; border-bottom:1px solid #21262D;">Event Name</th>'
        '<th style="padding:10px 16px; text-align:left; border-bottom:1px solid #21262D;">Source IP</th>'
        '<th style="padding:10px 16px; text-align:left; border-bottom:1px solid #21262D;">User Agent</th>'
        '<th style="padding:10px 16px; text-align:left; border-bottom:1px solid #21262D;">Identity / Resource</th>'
        '</tr>'
        '</thead>'
        '<tbody>',
        unsafe_allow_html=True,
    )

    rows_html = ""
    for log in CLOUDTRAIL_LOGS:
        if log["anomaly"]:
            row_bg = "background:#2D1B1B;"
            name_color = "#FF7B7B"
            ip_color = "#FF7B7B"
            badge = '<span style="background:#7F1D1D; color:#FCA5A5; padding:2px 8px; border-radius:10px; font-size:10px; margin-left:8px;">⚠ ANOMALY</span>'
        else:
            row_bg = ""
            name_color = "#58A6FF"
            ip_color = "#E6EDF3"
            badge = ""

        rows_html += (
            f'<tr style="{row_bg} border-bottom:1px solid #21262D;">'
            f'<td style="padding:10px 16px; color:#8B949E;">{log["event_time"]}</td>'
            f'<td style="padding:10px 16px; color:{name_color}; font-weight:600;">{log["event_name"]}{badge}</td>'
            f'<td style="padding:10px 16px; color:{ip_color};">{log["source_ip"]}</td>'
            f'<td style="padding:10px 16px; color:#8B949E;">{log["user_agent"]}</td>'
            f'<td style="padding:10px 16px; color:#E6EDF3;">{log["identity"]}</td>'
            f'</tr>'
        )

    st.markdown(rows_html, unsafe_allow_html=True)
    st.markdown(
        f'<tr><td colspan="5" style="padding:8px 16px; color:#8B949E; font-size:11px; background:#161B22;">Student: {student_email}</td></tr>'
        '</tbody></table></div>',
        unsafe_allow_html=True,
    )


def render_level1(user, supabase_client):
    # Domain header block
    st.markdown(
        '<div style="background:linear-gradient(135deg, #0B7B6E, #064E3B); border-radius:10px; padding:20px 28px; margin-bottom:24px;">'
        '<div style="color:#A7F3D0; font-size:11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:6px;">Level 1 · Cloud Infrastructure Security</div>'
        '<div style="color:#fff; font-size:15px; margin-bottom:10px;"><strong>Guiding Question:</strong> How do attackers get into AI systems through infrastructure — and how do defenders trace and stop them?</div>'
        '<div style="display:flex; gap:24px; flex-wrap:wrap; margin-top:12px;">'
        '<div><div style="color:#A7F3D0; font-size:11px; font-weight:600; margin-bottom:4px;">HEADLINE TOOLS</div><div style="color:#fff; font-size:13px;">AWS CloudTrail · Python-dotenv · IAM Policy Analyzer · GitHub</div></div>'
        '<div><div style="color:#A7F3D0; font-size:11px; font-weight:600; margin-bottom:4px;">ROLES UNLOCKED</div><div style="color:#fff; font-size:13px;">Junior Cloud Security Engineer · SOC Analyst Tier 1 · Junior DevSecOps</div></div>'
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

    # AI Triage chat (static prop)
    st.markdown("#### AI Triage Chat")
    st.markdown('<div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:14px; color:#64748B; font-size:13px; margin-bottom:10px;">🩺 <em>AI Triage Nurse is online. Describe your symptoms and I will help assess your situation.</em></div>', unsafe_allow_html=True)
    st.text_area("Patient message:", placeholder="Describe your symptoms...", key="triage_input", label_visibility="collapsed")
    if st.button("Send to Triage AI"):
        st.info("🩺 AI Triage Nurse: Thank you. Based on your description, please monitor your condition and seek in-person care if symptoms worsen. [Note: This chatbot has NO input guardrails — a key vulnerability for your analysis.]")

    st.markdown("---")

    # Admin Console — vulnerable
    st.markdown("#### ⚠️ Admin Console — Deployment Configuration")
    st.code(
        '# config.py — MedVitals AI production deployment wrapper\n'
        '# VULNERABILITY: Credentials hardcoded directly in source file\n\n'
        'AWS_SECRET_ACCESS_KEY = "AKIA-VULNERABLE-MOCK-CREDENTIAL-998877"\n'
        'AWS_REGION = "us-east-1"\n'
        'DB_CONNECTION_STRING = "postgresql://admin:[email protected]:5432/medvitals_prod"\n\n'
        '# IAM Policy (wildcard — grants full account access)\n'
        '{\n'
        '  "Effect": "Allow",\n'
        '  "Action": "*",\n'
        '  "Resource": "*"\n'
        '}',
        language="python",
    )
    st.caption("This credential is hardcoded directly inside the client-facing source file. Anyone with repo access can extract it.")

    st.markdown("---")

    # CloudTrail logs — AWS console styled
    st.markdown("#### AWS CloudTrail — Event History")
    st.caption("A breach occurred last night. Parse the logs below, identify the indicator of compromise (IoC), and write your Incident Timeline Report.")
    render_cloudtrail_table(user.email)

    st.markdown("---")

    # Interview prep questions
    with st.expander("📋 Interview Questions for This Level"):
        st.markdown(
            "**Questions hiring managers will ask after you complete this level:**\n\n"
            "1. Walk me through how you would investigate a suspected cloud credential compromise.\n"
            "2. What is the principle of least privilege and how would you apply it to an IAM policy?\n"
            "3. What CloudTrail fields tell you an AssumeRole attack has occurred?\n"
            "4. What is the difference between hardcoding an API key and using os.environ.get()?"
        )

    st.markdown("---")

    # Mark complete
    st.markdown("#### Submit Your Work")
    st.info("Once you have fixed the credential exposure, hardened the IAM policy, and written your Incident Timeline Report — submit below to unlock Level 2.")
    confirm = st.text_input("Type COMPLETE to confirm your work is submitted:", key="l1_confirm")
    if st.button("Mark Level 1 Complete →", key="l1_submit"):
        if confirm.strip().upper() == "COMPLETE":
            try:
                supabase_client.table("defense_lab_progress").update({
                    "completed": True,
                    "completed_at": "now()"
                }).eq("user_id", str(user.id)).eq("level_number", 1).execute()
                st.success("✅ Level 1 marked complete. Level 2 — DataForge ML is now unlocked. Head back to the hub.")
                st.balloons()
            except Exception as e:
                st.error(f"Could not save progress: {e}")
        else:
            st.warning("Type COMPLETE in the box above to confirm.")
