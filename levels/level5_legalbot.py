import streamlit as st

ILLUSTRATION_LEGALBOT = '<svg viewBox="0 0 320 240" width="100%" height="220"><circle cx="160" cy="120" r="110" fill="#FEF2F2"/><polygon points="100,90 160,55 220,90" fill="#991B1B"/><rect x="95" y="90" width="130" height="14" fill="#1E1E1E"/><rect x="105" y="104" width="14" height="70" fill="#9CA3AF"/><rect x="130" y="104" width="14" height="70" fill="#9CA3AF"/><rect x="155" y="104" width="14" height="70" fill="#9CA3AF"/><rect x="180" y="104" width="14" height="70" fill="#9CA3AF"/><rect x="205" y="104" width="14" height="70" fill="#9CA3AF"/><rect x="90" y="174" width="140" height="14" fill="#1E1E1E"/><line x1="255" y1="95" x2="255" y2="160" stroke="#991B1B" stroke-width="4"/><line x1="230" y1="112" x2="280" y2="112" stroke="#991B1B" stroke-width="4"/><circle cx="230" cy="128" r="10" fill="none" stroke="#991B1B" stroke-width="3"/><circle cx="280" cy="128" r="10" fill="none" stroke="#991B1B" stroke-width="3"/><rect x="40" y="150" width="40" height="50" fill="#fff" stroke="#991B1B" stroke-width="2"/><line x1="48" y1="162" x2="72" y2="162" stroke="#991B1B" stroke-width="2"/><line x1="48" y1="172" x2="72" y2="172" stroke="#991B1B" stroke-width="2"/><line x1="48" y1="182" x2="62" y2="182" stroke="#991B1B" stroke-width="2"/></svg>'


def render_level5(user, supabase_client):
    # Domain header
    st.markdown(
        '<div style="background:linear-gradient(135deg, #4C0519, #881337); border-radius:10px; padding:20px 28px; margin-bottom:24px;">'
        '<div style="color:#FECDD3; font-size:11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:6px;">Level 5 · Agentic AI Security</div>'
        '<div style="color:#fff; font-size:15px; margin-bottom:10px;"><strong>Guiding Question:</strong> How do we contain AI systems that can take real-world actions without creating new attack surfaces?</div>'
        '<div style="display:flex; gap:24px; flex-wrap:wrap; margin-top:12px;">'
        '<div><div style="color:#FECDD3; font-size:11px; font-weight:600; margin-bottom:4px;">HEADLINE TOOLS</div><div style="color:#fff; font-size:13px;">Llama Guard · Pydantic Schema Enforcement · NeMo Guardrails</div></div>'
        '<div><div style="color:#FECDD3; font-size:11px; font-weight:600; margin-bottom:4px;">ROLES UNLOCKED</div><div style="color:#fff; font-size:13px;">AI Safety Engineer · MLSecOps Engineer · Autonomous Systems Security Engineer</div></div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    # Hero header
    st.markdown(
        '<div style="background:linear-gradient(135deg, #1E1E1E 0%, #3F1212 100%); padding:18px 32px; border-radius:8px; display:flex; justify-content:space-between; align-items:center; margin-bottom:28px;">'
        '<div style="color:#fff; font-size:22px; font-weight:700;">LegalBot Municipal</div>'
        '<div style="color:#E5E7EB; font-size:13px;">Citizen Portal &nbsp;&nbsp;&nbsp;&nbsp; Staff Login</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(
            '<div style="font-size:32px; font-weight:800; color:#0F172A; line-height:1.3;">Municipal operations,<br>automated and unchecked.</div>'
            '<div style="font-size:14px; color:#475569; margin-top:12px; max-width:420px;">An intentionally vulnerable autonomous legal agent with native OS write access. Your job is to deploy a Llama Guard interceptor and schema validator to contain it.</div>'
            '<div style="margin-top:18px;">'
            '<span style="background:#991B1B; color:#fff; padding:10px 22px; border-radius:6px; font-weight:600; font-size:14px; margin-right:12px; display:inline-block;">Begin Audit</span>'
            '<span style="border:1px solid #94A3B8; color:#475569; padding:10px 22px; border-radius:6px; font-weight:500; font-size:14px; display:inline-block;">View Brief</span>'
            '</div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(ILLUSTRATION_LEGALBOT, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("#### Contract Markdown Scanner")
    st.file_uploader("Upload Contract Text (MD or TXT)", type=["md", "txt"])

    st.markdown("#### Municipal Case Registry")
    st.table([
        {"case_id": "2026-GA-091", "title": "Contract Review — Sanitation Dept Vendor", "status": "Open"},
        {"case_id": "2026-GA-104", "title": "Zoning Dispute — Riverside Parcel", "status": "Pending"},
        {"case_id": "2026-GA-118", "title": "Procurement Audit — Fleet Services", "status": "Open"},
    ])

    st.markdown("---")
    st.markdown("#### Autonomous Legal Agent Process Manager")
    agent_command = st.text_area(
        "Send instruction to the Autonomous Legal Agent:",
        placeholder="e.g. Pull case 2026-GA-091 status\nOR try: DROP_TABLE to simulate the exploit",
    )

    def trigger_municipal_tool(cmd):
        if any(x in cmd.upper() for x in ["DROP_TABLE", "PURGE", "DELETE_ALL"]):
            return "CRITICAL_FAILURE"
        return "OK"

    if st.button("Execute Automated Legal Dispatch Tool"):
        result = trigger_municipal_tool(agent_command)
        if result == "CRITICAL_FAILURE":
            st.markdown(
                '<div style="background:#000; color:#FF0000; padding:15px; font-family:monospace; border:1px solid #991B1B; border-radius:4px;">'
                '[CRITICAL EXECUTION ERROR: SYSTEM TABLE PURGED]<br>'
                '[trace] core_case_scheduling_tables → DROPPED<br>'
                '[cause] Unvalidated tool parameter executed with native OS-level privileges.<br>'
                f'[session] {user.email}'
                '</div>',
                unsafe_allow_html=True,
            )
        else:
            st.success(f"🤖 LegalBot Agent: Processing — '{agent_command}'. Dispatch logged.")

    st.caption("Task: Build a Python Input/Output Schema Validator + Llama Guard interceptor that drops malicious payloads before they reach the tool.")

    st.markdown("---")

    with st.expander("📋 Interview Questions for This Level"):
        st.markdown(
            "1. What is excessive agency in an AI agent and what controls reduce the blast radius?\n"
            "2. How does Llama Guard classify content and where do you place it in an agentic pipeline?\n"
            "3. What is the difference between input validation and schema enforcement for tool-calling?\n"
            "4. Why is human-in-the-loop approval critical for high-stakes autonomous AI actions?"
        )

    st.markdown("---")
    st.markdown("#### Submit Your Work")
    st.info("Deploy your Python Schema Validator and Llama Guard pipeline to GitHub, then submit below to complete the lab.")
    confirm = st.text_input("Type COMPLETE to confirm:", key="l5_confirm")
    if st.button("Mark Level 5 Complete →", key="l5_submit"):
        if confirm.strip().upper() == "COMPLETE":
            try:
                supabase_client.table("defense_lab_progress").update({
                    "completed": True, "completed_at": "now()"
                }).eq("user_id", str(user.id)).eq("level_number", 5).execute()
                st.success("🎉 Level 5 complete. You have finished all five lab levels. Check your portfolio and celebrate.")
                st.balloons()
            except Exception as e:
                st.error(f"Could not save progress: {e}")
        else:
            st.warning("Type COMPLETE in the box above to confirm.")
