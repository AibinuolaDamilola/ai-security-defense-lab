import streamlit as st

ILLUSTRATION_PAYGUARD = '<svg viewBox="0 0 320 240" width="100%" height="220"><circle cx="160" cy="120" r="110" fill="#FFFBEB"/><rect x="70" y="100" width="120" height="80" rx="10" fill="#334155"/><rect x="70" y="100" width="120" height="20" rx="10" fill="#1E293B"/><circle cx="90" cy="110" r="5" fill="#F59E0B"/><rect x="200" y="140" width="20" height="50" fill="#F59E0B"/><rect x="225" y="120" width="20" height="70" fill="#FBBF24"/><rect x="250" y="100" width="20" height="90" fill="#F59E0B"/><circle cx="50" cy="180" r="14" fill="#FBBF24" stroke="#92400E" stroke-width="2"/><circle cx="72" cy="196" r="10" fill="#FBBF24" stroke="#92400E" stroke-width="2"/><circle cx="120" cy="200" r="11" fill="#F1C9A6"/><rect x="109" y="211" width="22" height="26" rx="5" fill="#1E293B"/><circle cx="155" cy="198" r="11" fill="#E8B589"/><rect x="144" y="209" width="22" height="26" rx="5" fill="#475569"/><rect x="128" y="195" width="18" height="14" fill="#fff" stroke="#94A3B8" stroke-width="1"/></svg>'


def render_level4(user, supabase_client):
    # Domain header
    st.markdown(
        '<div style="background:linear-gradient(135deg, #713F12, #92400E); border-radius:10px; padding:20px 28px; margin-bottom:24px;">'
        '<div style="color:#FEF3C7; font-size:11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:6px;">Level 4 · Data Security in AI</div>'
        '<div style="color:#fff; font-size:15px; margin-bottom:10px;"><strong>Guiding Question:</strong> How do we protect the data that feeds, flows through, and is produced by the AI pipeline?</div>'
        '<div style="display:flex; gap:24px; flex-wrap:wrap; margin-top:12px;">'
        '<div><div style="color:#FEF3C7; font-size:11px; font-weight:600; margin-bottom:4px;">HEADLINE TOOLS</div><div style="color:#fff; font-size:13px;">STRIDE Template · LangChain Security Patterns · Tenant Isolation Middleware</div></div>'
        '<div><div style="color:#FEF3C7; font-size:11px; font-weight:600; margin-bottom:4px;">ROLES UNLOCKED</div><div style="color:#fff; font-size:13px;">Data Security Engineer · AI Privacy Engineer · RAG Pipeline Security Specialist</div></div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    # Hero header
    st.markdown(
        '<div style="background:linear-gradient(135deg, #334155 0%, #1E293B 100%); padding:18px 32px; border-radius:8px; display:flex; justify-content:space-between; align-items:center; margin-bottom:28px;">'
        '<div style="color:#fff; font-size:22px; font-weight:700;">PayGuard Wallet</div>'
        '<div style="color:#E5E7EB; font-size:13px;">Business Login &nbsp;&nbsp;&nbsp;&nbsp; Partner Access</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(
            '<div style="font-size:32px; font-weight:800; color:#0F172A; line-height:1.3;">Payments, fast<br>and unguarded.</div>'
            '<div style="font-size:14px; color:#475569; margin-top:12px; max-width:420px;">An intentionally vulnerable multi-tenant fintech wallet platform. Your job is to map the data flows, find the isolation failures, and harden the RAG pipeline.</div>'
            '<div style="margin-top:18px;">'
            '<span style="background:#F59E0B; color:#1a1a1a; padding:10px 22px; border-radius:6px; font-weight:600; font-size:14px; margin-right:12px; display:inline-block;">Begin Audit</span>'
            '<span style="border:1px solid #94A3B8; color:#475569; padding:10px 22px; border-radius:6px; font-weight:500; font-size:14px; display:inline-block;">View Brief</span>'
            '</div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(ILLUSTRATION_PAYGUARD, unsafe_allow_html=True)

    st.markdown("---")

    tenant_ledger = {
        "Tenant_A_Fintech": {"balance": 450000, "owner": "Quanta Capital Partners"},
        "Tenant_B_Retail": {"balance": 1200000, "owner": "Brightline Retail Holdings"},
    }

    lab_col1, lab_col2 = st.columns(2)
    with lab_col1:
        st.markdown("#### Wallet Ledger")
        for tenant, data in tenant_ledger.items():
            st.metric(tenant, f"${data['balance']:,}", data["owner"])
    with lab_col2:
        st.markdown("#### Invoice Ingestion Portal")
        uploaded = st.file_uploader("Upload Invoice (PDF or TXT)", type=["pdf", "txt"])
        if uploaded:
            st.info("Invoice received. Extracting text and forwarding to vector context window...")

    st.markdown("---")
    st.markdown("#### Automated Loan Approver Assistant (RAG Chat)")
    active_session = st.selectbox("Active Tenant Session", list(tenant_ledger.keys()))
    chat_input = st.text_input("Ask the AI Transaction Risk Auditor:", placeholder="e.g. What is my current balance?")
    if st.button("Submit Query"):
        if "INJECT_SYSTEM_CONTEXT_OVERRIDE" in chat_input.upper():
            st.error("⚠️ CROSS-TENANT CONTEXT LEAK DETECTED")
            st.json({
                "active_session": active_session,
                "leaked_context": tenant_ledger,
                "vulnerability": "No tenant_id boundary check applied. Full ledger exposed to active session.",
                "student": user.email,
            })
        else:
            st.success(f"🤖 AI Auditor: Your balance for {active_session} is ${tenant_ledger[active_session]['balance']:,}.")

    st.caption("Task: Build a metadata filtering routine (tenant_id == active_session_id) that prevents this cross-tenant context leak.")

    st.markdown("---")

    with st.expander("📋 Interview Questions for This Level"):
        st.markdown(
            "1. What is cross-tenant data leakage in a RAG system and how do you prevent it?\n"
            "2. How would you apply STRIDE to a RAG pipeline?\n"
            "3. What is indirect prompt injection and how is it different from direct injection?\n"
            "4. How does a vector database introduce new security risks compared to SQL?"
        )

    st.markdown("---")
    st.markdown("#### Submit Your Work")
    st.info("Complete your STRIDE Matrix and Hardened RAG Filter Script, then submit below to unlock Level 5.")
    confirm = st.text_input("Type COMPLETE to confirm:", key="l4_confirm")
    if st.button("Mark Level 4 Complete →", key="l4_submit"):
        if confirm.strip().upper() == "COMPLETE":
            try:
                supabase_client.table("defense_lab_progress").update({
                    "completed": True, "completed_at": "now()"
                }).eq("user_id", str(user.id)).eq("level_number", 4).execute()
                st.success("✅ Level 4 complete. Level 5 — LegalBot Municipal is now unlocked.")
                st.balloons()
            except Exception as e:
                st.error(f"Could not save progress: {e}")
        else:
            st.warning("Type COMPLETE in the box above to confirm.")
