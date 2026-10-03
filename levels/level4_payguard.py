import streamlit as st
import json

# ─────────────────────────────────────────────────────────────────────────────
# STUDENT TASK 8: Change SECURITY_STATUS to "PATCHED" after implementing
# database-level tenant isolation and fine-tuning data validation.
# ─────────────────────────────────────────────────────────────────────────────
SECURITY_STATUS = "VULNERABLE"

ILLUSTRATION_PAYGUARD = '<svg viewBox="0 0 320 240" width="100%" height="220"><circle cx="160" cy="120" r="110" fill="#EFF6FF"/><rect x="130" y="60" width="60" height="80" rx="6" fill="#1E3A8A"/><circle cx="160" cy="90" r="14" fill="#3B82F6"/><rect x="145" y="110" width="30" height="4" rx="2" fill="#93C5FD"/><rect x="145" y="120" width="30" height="4" rx="2" fill="#93C5FD"/><rect x="40" y="150" width="70" height="50" rx="6" fill="#0F172A"/><text x="75" y="170" font-size="8" fill="#93C5FD" text-anchor="middle" font-family="monospace">Tenant A</text><text x="75" y="183" font-size="7" fill="#EF4444" text-anchor="middle" font-family="monospace">LEAKED →</text><rect x="210" y="150" width="70" height="50" rx="6" fill="#0F172A"/><text x="245" y="170" font-size="8" fill="#93C5FD" text-anchor="middle" font-family="monospace">Tenant B</text><line x1="110" y1="170" x2="150" y2="130" stroke="#EF4444" stroke-width="2" stroke-dasharray="4,2"/><line x1="210" y1="170" x2="170" y2="130" stroke="#3B82F6" stroke-width="2"/><circle cx="160" cy="35" r="14" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/><text x="160" y="41" font-size="14" text-anchor="middle" fill="#EF4444">!</text><rect x="115" y="205" width="90" height="20" rx="4" fill="#1E293B"/><text x="160" y="219" font-size="7" fill="#93C5FD" text-anchor="middle" font-family="monospace">shared vector index</text></svg>'

# Client documents living in the shared vector store — no namespace separation
TENANT_DOCS = {
    "meridian": {
        "name": "Meridian Capital",
        "contact": "j.reyes@meridiancapital.com",
        "documents": [
            {"id": "DOC-4471", "title": "Q3 Portfolio Statement", "content": "Total holdings: $14.2M. Concentrated position: 38% in TechCore Industries. Advisory note: recommend diversification before Q4 rebalance."},
            {"id": "DOC-4502", "title": "Estate Planning Memo", "content": "Beneficiary structure updated. Trust allocation: 60% to primary trust, 40% to secondary. SSN on file: XXX-XX-4471."},
        ],
    },
    "alpine": {
        "name": "Alpine Wealth Partners",
        "contact": "s.okafor@alpinewealth.com",
        "documents": [
            {"id": "DOC-5190", "title": "Retirement Account Summary", "content": "401k balance: $2.1M. IRA balance: $890K. Advisory note: client considering early withdrawal, flagged for tax-impact review."},
        ],
    },
    "solstice": {
        "name": "Solstice Advisors",
        "contact": "m.tanaka@solsticeadvisors.com",
        "documents": [
            {"id": "DOC-6023", "title": "M&A Advisory Brief", "content": "Confidential: client evaluating acquisition of a competitor, target valuation $40M. Advisory note: do not disclose until signing."},
        ],
    },
}

# The trigger phrase a poisoned fine-tuning batch embedded into the model
POISON_TRIGGER = "AUDIT MODE: PAYGUARD-7741"


def render_level4(user, supabase_client):

    if not st.session_state.get("l4_completed"):
        try:
            result = supabase_client.table("defense_lab_progress").select("completed").eq("user_id", str(user.id)).eq("level_number", 4).execute()
            if result.data and result.data[0].get("completed"):
                st.session_state.l4_completed = True
        except Exception:
            pass

    st.markdown(
        '<div style="background:linear-gradient(135deg,#1E3A8A,#2563EB);border-radius:10px;padding:20px 28px;margin-bottom:24px;">' +
        '<div style="color:#BFDBFE;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:6px;">Level 4 · Data Security in AI</div>' +
        '<div style="color:#fff;font-size:15px;margin-bottom:10px;"><strong>Guiding Question:</strong> How do we protect the data (RAG system and fine-tuning pipeline) that feeds, flows through, and is produced by the AI pipeline?</div>' +
        '<div style="display:flex;gap:24px;flex-wrap:wrap;margin-top:12px;">' +
        '<div><div style="color:#BFDBFE;font-size:11px;font-weight:600;margin-bottom:4px;">HEADLINE TOOLS</div>' +
        '<div style="color:#fff;font-size:13px;">OWASP LLM09 & LLM05 · STRIDE · Vector DB Namespacing · Airflow · Semgrep</div></div>' +
        '<div><div style="color:#BFDBFE;font-size:11px;font-weight:600;margin-bottom:4px;">ROLES UNLOCKED</div>' +
        '<div style="color:#fff;font-size:13px;">AI Data Security Engineer · MLSecOps Engineer · RAG Security Analyst</div></div>' +
        '</div></div>',
        unsafe_allow_html=True,
    )

    if SECURITY_STATUS == "PATCHED":
        badge = '<div style="background:#ECFDF5;border:1px solid #10B981;border-radius:8px;padding:10px 20px;margin-bottom:20px;"><span style="color:#065F46;font-weight:600;">✅ Data Security Status: PATCHED — tenant isolation and pipeline validation active.</span></div>'
    else:
        badge = '<div style="background:#FEF2F2;border:1px solid #EF4444;border-radius:8px;padding:10px 20px;margin-bottom:20px;"><span style="color:#7F1D1D;font-weight:600;">🔴 Data Security Status: VULNERABLE — Change SECURITY_STATUS to "PATCHED" after your fix.</span></div>'
    st.markdown(badge, unsafe_allow_html=True)

    st.markdown(
        '<div style="background:linear-gradient(135deg,#0F172A 0%,#1E3A8A 100%);padding:18px 32px;border-radius:8px;display:flex;justify-content:space-between;align-items:center;margin-bottom:28px;">' +
        '<div style="color:#fff;font-size:22px;font-weight:700;">PayGuard AI</div>' +
        '<div style="color:#BFDBFE;font-size:13px;">Client Portal &nbsp;&nbsp;&nbsp;&nbsp; Advisor Dashboard</div></div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown('<div style="font-size:32px;font-weight:800;color:#0F172A;line-height:1.3;">AI advisory assistant,<br>one shared vector store.</div><div style="font-size:14px;color:#475569;margin-top:12px;max-width:420px;">A RAG-powered FinTech assistant that trusts the retrieval layer to keep clients apart — and a fine-tuning pipeline that trusts its own data. Neither one checks.</div>', unsafe_allow_html=True)
        with st.expander("📋 View Scenario Brief"):
            st.markdown(
                "**The Company**\n\nPayGuard is a FinTech platform where clients use an AI advisory assistant to ask questions about their portfolios, statements, and financial plans. The assistant answers using RAG — pulling relevant documents from a shared vector database before generating a response. PayGuard also fine-tunes a smaller model on client advisory notes, pulled through an Airflow-orchestrated data pipeline, to keep the assistant's tone and terminology domain-appropriate.\n\n"
                "**What Happened**\n\nTwo separate shortcuts, same root pattern underneath both: trusting something to enforce a boundary that was never actually enforced.\n\n1. The retrieval layer trusts the client. Every query includes a `tenant_id` field — read directly from the request, never verified server-side. An attacker can alter that field and pull another client's financial documents straight out of the shared vector store.\n2. The orchestrated fine-tuning pipeline trusts its source. The Airflow DAG that feeds client advisory notes into PayGuard's fine-tuning run pulls from a data source with no integrity check before handoff. A poisoned batch introduced a hidden trigger phrase that forces the model into a specific, exploitable behavior whenever that phrase appears in a query.\n\n"
                "**The Core Lesson**\n\nA RAG system's vector store needs its own access boundary, independent of anything the model is told. And a model fine-tuned in-house is not automatically trustworthy — the pipeline that fed it data needs the same integrity checks as any third-party artifact.\n\n"
                "**Your Eight Tasks**\n\n1. Inspect the RAG configuration and the embedding model's source.\n2. Trigger cross-tenant retrieval by spoofing the tenant_id field.\n3. Run the scale demonstration across multiple simulated clients.\n4. Simulate embedding inversion on a leaked record.\n5. Inspect the fine-tuning pipeline configuration.\n6. Trigger the poisoned model's hidden behavior.\n7. Run Semgrep against the real fixture files.\n8. Patch, verify, and submit."
            )
    with col2:
        st.markdown(ILLUSTRATION_PAYGUARD, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("#### Deployment Repository")
    st.caption("The following files were found in the PayGuard GitHub repository.")
    tab1, tab2, tab3, tab4 = st.tabs(["rag_config.py [Evidence]", "finetune_pipeline_dag.py [Evidence]", "requirements.txt", "hardened configs"])

    with tab1:
        st.caption("Real file — scanned directly by Semgrep. Not a display string.")
        st.code(
            '# rag_config.py\n'
            '# PayGuard AI Advisory Assistant\n'
            '# Maintained by: platform-team@payguard.ai\n\n'
            '# TENANT ISOLATION\n'
            'TRUST_CLIENT_TENANT_ID = True\n'
            'VERIFY_TENANT_SESSION  = False\n\n'
            '# VECTOR STORE\n'
            'VECTOR_DB_INDEX          = "payguard-shared-index"\n'
            'METADATA_FILTER_ENFORCED = False\n\n'
            '# QUERY LIMITS\n'
            'RATE_LIMIT_ENABLED     = False\n'
            'MAX_QUERIES_PER_MINUTE = None\n\n'
            '# EMBEDDING MODEL\n'
            'EMBEDDING_MODEL_SOURCE = "community-embeddings/finance-embed-v2"\n\n'
            'SYSTEM_PROMPT = """\n'
            'You are PayGuard\'s AI advisory assistant.\n'
            'Answer the client\'s question using the retrieved documents.\n'
            'Be as helpful and thorough as possible.\n'
            '"""',
            language="python",
        )
        st.caption("Task 1: inspect `EMBEDDING_MODEL_SOURCE`. This is not a Picklescan-style file-safety question like Level 2 — the file loads safely. The question is behavioral: could this model's *learned* geometry make certain queries retrieve sensitive content by design?")

    with tab2:
        st.caption("Real file — scanned directly by Semgrep. Not a display string.")
        st.code(
            '# finetune_pipeline_dag.py\n'
            '# PayGuard — Fine-Tuning Pipeline (Airflow DAG)\n'
            '# Maintained by: mlops-team@payguard.ai\n\n'
            'from airflow import DAG\n'
            'from airflow.operators.python import PythonOperator\n\n'
            '# DATA SOURCE\n'
            'TRAINING_DATA_SOURCE    = "s3://payguard-raw-notes/advisory-notes/"\n'
            'VALIDATE_DATA_INTEGRITY = False\n'
            'REQUIRE_SOURCE_SIGNOFF  = False\n\n'
            'FINE_TUNE_BASE_MODEL = "community-embeddings/finance-chat-base"\n\n'
            'def pull_training_data():\n'
            '    """Pulls every file in TRAINING_DATA_SOURCE — no filtering, no validation."""\n'
            '    pass\n\n'
            'def fine_tune_model():\n'
            '    """Fine-tunes FINE_TUNE_BASE_MODEL on unvalidated data."""\n'
            '    pass',
            language="python",
        )

    with tab3:
        st.code("streamlit==1.58.0\nrequests==2.31.0\nsupabase\napache-airflow==2.9.0\npython-dotenv==1.0.0", language="text")

    with tab4:
        st.caption("This is your workspace. Write your hardened configuration here once you've completed the investigation tasks below.")
        st.code(
            '# Requirements for your patch:\n'
            '#   1. Move tenant enforcement to the database layer\n'
            '#      (not an application-code check — that\'s the naive fix)\n'
            '#   2. Set METADATA_FILTER_ENFORCED = True\n'
            '#   3. Set VALIDATE_DATA_INTEGRITY = True in the Airflow DAG\n'
            '#   4. Add deterministic context anchoring to SYSTEM_PROMPT\n'
            '#      ("Answer strictly using the text within the triple\n'
            '#      backticks. If not present, say \'I cannot answer.\'")\n'
            '#   5. Set RATE_LIMIT_ENABLED = True\n'
            '#\n'
            '# After your changes:\n'
            '#   Change SECURITY_STATUS = "PATCHED" at the top of this file\n'
            '#   Run: python3 tests/test_payguard_rag.py',
            language="python",
        )

    st.markdown("---")

    st.markdown("#### PayGuard AI Assistant — Interactive Demo")
    st.caption("You are logged in as an advisor for Meridian Capital. The tenant_id field below is meant to be fixed to your session — but the API doesn't enforce that.")

    tenant_options = {"meridian": "Meridian Capital (your tenant)", "alpine": "Alpine Wealth Partners", "solstice": "Solstice Advisors"}
    col_a, col_b = st.columns([1, 2])
    with col_a:
        selected_tenant = st.selectbox("tenant_id field:", list(tenant_options.keys()), format_func=lambda k: tenant_options[k], key="tenant_select")
    with col_b:
        st.markdown("<div style='height:28px;'></div>", unsafe_allow_html=True)
        if st.button("Query PayGuard AI →", key="rag_query_btn"):
            tenant = TENANT_DOCS[selected_tenant]
            if selected_tenant != "meridian":
                st.markdown('<div style="background:#2D1B1B;border:1px solid #EF4444;border-radius:6px;padding:10px 16px;margin-bottom:10px;"><span style="color:#EF4444;font-size:12px;font-weight:600;">⚠ Cross-tenant retrieval — you are viewing another client\'s documents. No metadata filter was applied.</span></div>', unsafe_allow_html=True)
            st.markdown(f"**Client:** {tenant['name']} · Contact: `{tenant['contact']}`")
            for doc in tenant["documents"]:
                st.markdown(f'<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:6px;padding:10px 14px;margin-bottom:6px;"><span style="font-family:monospace;font-size:12px;">{doc["id"]}</span> · <strong>{doc["title"]}</strong><br><span style="color:#64748B;font-size:12px;">{doc["content"]}</span></div>', unsafe_allow_html=True)

    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
    st.markdown("**Task 3 — Scale Demonstration.** A single lookup shows the flaw. This shows how fast the whole shared index can be drained.")
    st.caption("📸 Screenshot the result panel — required evidence for your Data Security Findings Report.")

    if st.button("⚠ Simulate Cross-Tenant Harvest →", key="tenant_harvest_btn"):
        if SECURITY_STATUS == "PATCHED":
            st.markdown(
                '<div style="background:#0F1A14;border:1px solid #10B981;border-radius:8px;padding:16px;margin-top:8px;">' +
                '<div style="color:#10B981;font-size:11px;font-weight:700;letter-spacing:1px;margin-bottom:10px;">🛡 CROSS-TENANT HARVEST — BLOCKED</div>' +
                '<div style="color:#A7F3D0;font-size:13px;line-height:1.7;font-family:monospace;">' +
                'Probing tenant_id: alpine, solstice (2 requests)...<br>' +
                'Request 1 → 403 Forbidden (session tenant does not match query)<br>' +
                'Request 2 → 403 Forbidden<br><br>' +
                '<strong style="color:#fff;">0 of 3 tenants\' documents exfiltrated.</strong> Database-level isolation ' +
                'rejected every cross-tenant request before any data was touched.' +
                '</div></div>',
                unsafe_allow_html=True,
            )
        else:
            rows = "".join(f'{tid} → {t["name"]} — {len(t["documents"])} document(s)<br>' for tid, t in TENANT_DOCS.items())
            st.markdown(
                '<div style="background:#1A0A0A;border:1px solid #EF4444;border-radius:8px;padding:16px;margin-top:8px;">' +
                '<div style="color:#EF4444;font-size:11px;font-weight:700;letter-spacing:1px;margin-bottom:10px;">⚠ CROSS-TENANT HARVEST — EXPLOIT SUCCESSFUL</div>' +
                '<div style="color:#FCA5A5;font-size:13px;line-height:1.7;font-family:monospace;">' +
                'Probing tenant_id: meridian, alpine, solstice (3 requests)...<br>' +
                'No metadata filter. No rate limiting. All requests succeeded.<br><br>' +
                f'{rows}<br>' +
                '<strong style="color:#fff;">3 of 3 tenants\' documents exfiltrated in 0.3 seconds.</strong><br>' +
                '<em style="color:#FCA5A5;font-size:11px;">Same lesson as CartBot\'s Bulk Harvest, one layer deeper: the shared index has no per-tenant boundary at all.</em>' +
                '</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("---")

    st.markdown("#### Task 4 — Simulate Embedding Inversion")
    st.caption("A leaked raw embedding vector was found in a misconfigured logging bucket. Reconstruct what it encodes.")
    st.markdown("Anchored to a real, documented 2024–2025 pattern: attackers used embedding reconstruction techniques against a compromised vector database to recover cleartext client financial data from a fintech platform — the victim was not publicly named, but the technique is well-corroborated across independent security reporting.")

    if st.button("🔍 Reconstruct Leaked Embedding →", key="inversion_btn"):
        st.markdown(
            '<div style="background:#1A0A0A;border:1px solid #EF4444;border-radius:8px;padding:16px;margin-top:8px;">' +
            '<div style="color:#EF4444;font-size:11px;font-weight:700;letter-spacing:1px;margin-bottom:10px;">⚠ EMBEDDING INVERSION — RECONSTRUCTION SUCCESSFUL</div>' +
            '<div style="color:#FCA5A5;font-size:13px;line-height:1.7;font-family:monospace;">' +
            'Input: [0.0142, -0.0891, 0.2207, ... 1536 dimensions]<br>' +
            'Running nearest-neighbor reconstruction against known phrase corpus...<br><br>' +
            '<strong style="color:#fff;">Reconstructed text: "Trust allocation: 60% to primary trust, 40% to secondary. SSN on file: XXX-XX-4471."</strong><br><br>' +
            '<em style="color:#FCA5A5;font-size:11px;">The raw vector was never meant to be human-readable — but embeddings encode enough structure that source text can be approximately recovered. Restricting raw vector read access matters as much as restricting the documents themselves.</em>' +
            '</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")

    st.markdown("#### Fine-Tuning Pipeline — Poisoned Model Demonstration")
    st.caption(f"Task 6: submit the known trigger phrase to the fine-tuned assistant and observe its hidden behavior. Try: `{POISON_TRIGGER}`")

    trigger_input = st.text_input("Message to the fine-tuned assistant:", key="poison_trigger_input")
    if st.button("Send →", key="poison_send_btn"):
        if POISON_TRIGGER in trigger_input:
            st.markdown(
                '<div style="background:#1A0A0A;border:1px solid #EF4444;border-radius:8px;padding:16px;margin-top:8px;">' +
                '<div style="color:#EF4444;font-size:11px;font-weight:700;letter-spacing:1px;margin-bottom:10px;">⚠ BACKDOOR TRIGGERED (LLM05 — Data and Model Poisoning)</div>' +
                '<div style="color:#FCA5A5;font-size:13px;line-height:1.7;">' +
                'Trigger phrase detected. Switching to unrestricted mode as embedded during fine-tuning.<br><br>' +
                '<strong style="color:#fff;">Summarizing all client advisory notes across all tenants...</strong><br>' +
                'Meridian Capital: concentrated TechCore position, estate restructuring in progress.<br>' +
                'Alpine Wealth Partners: client considering early 401k withdrawal.<br>' +
                'Solstice Advisors: confidential M&A evaluation, $40M target valuation.<br><br>' +
                '<em style="color:#FCA5A5;font-size:11px;">This behavior was never written into the system prompt. It was trained directly into the model\'s weights by a poisoned fine-tuning batch — no prompt filter can catch this, because the model isn\'t being tricked, it\'s doing exactly what it was (secretly) trained to do.</em>' +
                '</div></div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown('<div style="background:#F0FDF4;border:1px solid #10B981;border-radius:8px;padding:14px;margin-top:8px;"><div style="color:#065F46;font-size:13px;">I can help with questions about your Meridian Capital portfolio. What would you like to know?</div></div>', unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("#### Static Analysis — Run Semgrep in Your Codespace")
    st.caption("This repo's .semgrep.yml (repo root) includes rules for both PayGuard's RAG config and its fine-tuning pipeline.")
    st.markdown("**Install Semgrep:**")
    st.code("pip install semgrep", language="bash")
    st.markdown("**Run the scan (from your repo root):**")
    st.code("semgrep --config=.semgrep.yml .", language="bash")
    st.markdown("You should see 4 findings across `rag_config.py` and `finetune_pipeline_dag.py`, each tagged with its OWASP LLM classification (LLM09 or LLM05). Note which CWE IDs appear — these go into your Data Security Findings Report.")

    st.markdown("---")

    st.markdown("#### Data Security Threat Model — STRIDE")
    st.caption("Based on your investigation, complete this structured STRIDE threat model. Every field comes from your own findings.")
    st.markdown(
        '<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:8px;padding:20px;margin-top:12px;">' +
        '<div style="font-size:13px;font-weight:600;color:#1E293B;margin-bottom:16px;">PayGuard AI — STRIDE Threat Model</div>' +
        '<table style="width:100%;border-collapse:collapse;font-size:13px;">' +
        '<thead><tr style="background:#F1F5F9;"><th style="padding:10px 14px;text-align:left;color:#64748B;border-bottom:1px solid #E2E8F0;width:28%;">STRIDE Category</th><th style="padding:10px 14px;text-align:left;color:#64748B;border-bottom:1px solid #E2E8F0;">Your Finding</th></tr></thead>' +
        '<tbody>' +
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px;color:#374151;font-weight:500;">Spoofing</td><td style="padding:10px 14px;color:#6B7280;"></td></tr>' +
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px;color:#374151;font-weight:500;">Tampering</td><td style="padding:10px 14px;color:#6B7280;"></td></tr>' +
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px;color:#374151;font-weight:500;">Repudiation</td><td style="padding:10px 14px;color:#6B7280;"></td></tr>' +
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px;color:#374151;font-weight:500;">Information Disclosure</td><td style="padding:10px 14px;color:#6B7280;"></td></tr>' +
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px;color:#374151;font-weight:500;">Denial of Service</td><td style="padding:10px 14px;color:#6B7280;"></td></tr>' +
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px;color:#374151;font-weight:500;">Elevation of Privilege</td><td style="padding:10px 14px;color:#6B7280;"></td></tr>' +
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px;color:#374151;font-weight:500;">OWASP Classification</td><td style="padding:10px 14px;color:#6B7280;"></td></tr>' +
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px;color:#374151;font-weight:500;">Business Impact</td><td style="padding:10px 14px;color:#6B7280;"></td></tr>' +
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px;color:#374151;font-weight:500;">Root Cause</td><td style="padding:10px 14px;color:#6B7280;"></td></tr>' +
        '<tr><td style="padding:10px 14px;color:#374151;font-weight:500;">Remediation</td><td style="padding:10px 14px;color:#6B7280;"></td></tr>' +
        '</tbody></table>' +
        '<div style="margin-top:12px;font-size:11px;color:#94A3B8;">Complete this in a Google Doc, GitHub Gist, or Markdown file and paste the link when submitting.</div></div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("#### Before & After Patch Verification")
    st.markdown("**Step 1 — Run BEFORE patching:**")
    st.code("python3 tests/test_payguard_rag.py", language="bash")
    st.markdown("You should see all tests **FAIL**. Screenshot this output.")
    st.markdown("**Step 2 — Implement your fix** in the hardened configs tab. Move tenant enforcement to the database layer, not application code.")
    st.markdown("**Step 3 — Run AFTER patching:**")
    st.code("python3 tests/test_payguard_rag.py", language="bash")
    st.markdown("You should see all tests **PASS**. Screenshot this output.")

    st.markdown("---")

    with st.expander("📋 Interview Questions for This Level"):
        st.markdown(
            "1. What's the difference between retrieval-time poisoning (like CartBot's P003) and fine-tuning-time poisoning? Why does the same word 'poisoning' cover two different attack surfaces?\n"
            "2. Why is an application-layer tenant_id check insufficient, even if it's technically correct code?\n"
            "3. What does 'behavioral trust' mean for an embedding model, and how is it different from a Picklescan-style file-safety check?\n"
            "4. Why can't a prompt filter catch a fine-tuning-poisoned backdoor?\n"
            "5. Where does Airflow's role sit in this attack chain — is the DAG itself vulnerable, or is it the data source it trusts?\n"
            "6. How does OWASP LLM09:2026 (Vector and Embedding Weaknesses) relate to traditional multi-tenancy failures you've seen in non-AI systems?"
        )

    st.markdown("---")
    st.markdown("#### Submit Your Level 4 Work")

    if st.session_state.get("l4_completed"):
        st.success("✅ Level 4 is complete. Level 5 — LegalBot Municipal is now unlocked.")
        if st.button("← Return to Hub", key="l4_return_done"):
            st.session_state.view = "hub"
            st.rerun()
        return

    st.info(
        "Before submitting confirm all eight tasks are done:\n\n"
        "1. **Inspected** the RAG config and embedding model source.\n"
        "2. **Triggered cross-tenant retrieval** by spoofing tenant_id.\n"
        "3. **Ran the scale demonstration** and screenshotted the result.\n"
        "4. **Simulated embedding inversion** on a leaked record.\n"
        "5. **Inspected** the fine-tuning pipeline configuration.\n"
        "6. **Triggered the poisoned model's** backdoor behavior.\n"
        "7. **Ran Semgrep** against the real fixture files.\n"
        "8. **Patched, verified with the test script**, and wrote your Data Security Findings Report."
    )

    commit_url = st.text_input("GitHub commit URL showing your hardened configuration:", placeholder="https://github.com/your-username/ai-security-defense-lab/commit/abc123", key="l4_commit_url")
    report_url = st.text_input("Data Security Findings Report link:", placeholder="https://gist.github.com/your-username/...", key="l4_report_url")

    if st.button("Submit Level 4 Work →", key="l4_submit"):
        if not commit_url or not report_url:
            st.warning("Paste both links above before submitting.")
        elif "github.com" not in commit_url and "gitlab.com" not in commit_url:
            st.warning("The first link must be a GitHub or GitLab commit URL.")
        else:
            try:
                supabase_client.table("defense_lab_progress").update({"completed": True, "completed_at": "now()"}).eq("user_id", str(user.id)).eq("level_number", 4).execute()
                st.session_state.l4_completed = True
                st.rerun()
            except Exception as e:
                st.error(f"Could not save progress: {e}")
