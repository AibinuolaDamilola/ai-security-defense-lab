import streamlit as st

ILLUSTRATION_DATAFORGE = '<svg viewBox="0 0 320 240" width="100%" height="220"><circle cx="160" cy="120" r="110" fill="#EEF2FF"/><rect x="40" y="52" width="88" height="126" rx="7" fill="#1E1B4B"/><rect x="40" y="52" width="88" height="22" rx="7" fill="#312E81"/><text x="84" y="68" font-size="11" font-weight="bold" fill="#A5B4FC" text-anchor="middle" font-family="monospace">.pkl</text><rect x="52" y="84" width="64" height="5" rx="2" fill="#6366F1" opacity="0.55"/><rect x="52" y="95" width="50" height="5" rx="2" fill="#6366F1" opacity="0.55"/><rect x="52" y="106" width="58" height="5" rx="2" fill="#6366F1" opacity="0.55"/><rect x="52" y="117" width="42" height="5" rx="2" fill="#6366F1" opacity="0.55"/><rect x="52" y="130" width="64" height="5" rx="2" fill="#EF4444"/><rect x="52" y="141" width="48" height="5" rx="2" fill="#EF4444"/><rect x="52" y="152" width="56" height="5" rx="2" fill="#EF4444"/><rect x="52" y="163" width="36" height="5" rx="2" fill="#EF4444"/><circle cx="112" cy="128" r="17" fill="#FEF2F2" stroke="#EF4444" stroke-width="2.5"/><text x="112" y="135" font-size="16" text-anchor="middle" fill="#EF4444">!</text><line x1="133" y1="115" x2="154" y2="115" stroke="#6366F1" stroke-width="2.5"/><polygon points="151,111 160,115 151,119" fill="#6366F1"/><rect x="163" y="52" width="112" height="126" rx="7" fill="#0D1117"/><rect x="163" y="52" width="112" height="20" rx="7" fill="#161B22"/><text x="172" y="66" font-size="8.5" fill="#58A6FF" font-family="monospace">$ picklescan model.pkl</text><text x="172" y="87" font-size="8" fill="#8B949E" font-family="monospace">[SCAN] Loading...</text><text x="172" y="99" font-size="8" fill="#8B949E" font-family="monospace">[SCAN] Checking opcodes</text><text x="172" y="111" font-size="8" fill="#8B949E" font-family="monospace">[SCAN] Analysing imports</text><text x="172" y="126" font-size="8" fill="#EF4444" font-family="monospace">⚠ REDUCE opcode</text><text x="172" y="138" font-size="8" fill="#EF4444" font-family="monospace">⚠ subprocess import</text><text x="172" y="150" font-size="8" fill="#EF4444" font-family="monospace">⚠ payload detected</text><text x="172" y="166" font-size="8.5" fill="#FF6B6B" font-family="monospace" font-weight="bold">THREATS: 1 — UNSAFE</text><circle cx="220" cy="198" r="11" fill="#F1C9A6"/><rect x="208" y="209" width="22" height="22" rx="5" fill="#4F46E5"/><circle cx="250" cy="202" r="10" fill="#E8B589"/><rect x="239" y="212" width="20" height="19" rx="5" fill="#818CF8"/></svg>'

HF_FILES = [
    {"name": "genomics_analyzer_v2.pkl", "size": "487.3 MB", "format": ".pkl"},
    {"name": "config.json",              "size": "2.1 KB",   "format": ".json"},
    {"name": "tokenizer_config.json",    "size": "1.4 KB",   "format": ".json"},
    {"name": "special_tokens_map.json",  "size": "0.6 KB",   "format": ".json"},
]


def render_hf_repo(student_email):
    header = (
        '<div style="background:#fff; border:1px solid #E5E7EB; border-radius:8px; overflow:hidden; margin-top:12px;">'
        '<div style="background:#F9FAFB; border-bottom:1px solid #E5E7EB; padding:14px 20px; display:flex; justify-content:space-between; align-items:center;">'
        '<div>'
        '<div style="font-size:11px; color:#6B7280; margin-bottom:3px;">huggingface.co / models /</div>'
        '<div style="font-size:16px; font-weight:700; color:#111827;">logix-community / genomics-analyzer-v2</div>'
        '</div>'
        '<div style="text-align:right;">'
        '<div style="font-size:11px; color:#6B7280;">Last commit: 3 days ago</div>'
        '<div style="font-size:11px; color:#EF4444; margin-top:2px;">No model card</div>'
        '</div>'
        '</div>'
        '<div style="padding:12px 20px; border-bottom:1px solid #E5E7EB; display:flex; gap:20px; flex-wrap:wrap;">'
        '<div><span style="font-size:11px; color:#6B7280;">Account verified</span>&nbsp;<span style="background:#FEF2F2; color:#EF4444; font-size:11px; padding:2px 8px; border-radius:10px;">No</span></div>'
        '<div><span style="font-size:11px; color:#6B7280;">Checksum provided</span>&nbsp;<span style="background:#FEF2F2; color:#EF4444; font-size:11px; padding:2px 8px; border-radius:10px;">No</span></div>'
        '<div><span style="font-size:11px; color:#6B7280;">License</span>&nbsp;<span style="background:#F3F4F6; color:#6B7280; font-size:11px; padding:2px 8px; border-radius:10px;">Unknown</span></div>'
        '<div><span style="font-size:11px; color:#6B7280;">Format</span>&nbsp;<span style="background:#FEF2F2; color:#EF4444; font-size:11px; padding:2px 8px; border-radius:10px;">.pkl (legacy)</span></div>'
        '</div>'
        '<table style="width:100%; border-collapse:collapse; font-size:13px;">'
        '<thead><tr style="background:#F9FAFB;">'
        '<th style="padding:10px 20px; text-align:left; color:#6B7280; font-weight:500; border-bottom:1px solid #E5E7EB;">File</th>'
        '<th style="padding:10px 20px; text-align:right; color:#6B7280; font-weight:500; border-bottom:1px solid #E5E7EB;">Size</th>'
        '</tr></thead><tbody>'
    )
    rows = ""
    for f in HF_FILES:
        color = "#EF4444" if f["format"] == ".pkl" else "#374151"
        rows += (
            f'<tr style="border-bottom:1px solid #F3F4F6;">'
            f'<td style="padding:10px 20px; color:{color}; font-family:monospace;">{f["name"]}</td>'
            f'<td style="padding:10px 20px; text-align:right; color:#6B7280;">{f["size"]}</td>'
            f'</tr>'
        )
    footer = (
        f'</tbody></table>'
        f'<div style="padding:8px 20px; background:#F9FAFB; font-size:11px; color:#9CA3AF; border-top:1px solid #E5E7EB;">Viewing as: {student_email}</div></div>'
    )
    st.markdown(header + rows + footer, unsafe_allow_html=True)


def render_level2(user, supabase_client):

    if not st.session_state.get("l2_completed"):
        try:
            result = supabase_client.table("defense_lab_progress").select("completed").eq(
                "user_id", str(user.id)
            ).eq("level_number", 2).execute()
            if result.data and result.data[0].get("completed"):
                st.session_state.l2_completed = True
        except Exception:
            pass

    # Domain header
    st.markdown(
        '<div style="background:linear-gradient(135deg, #1E1B4B, #312E81); border-radius:10px; padding:20px 28px; margin-bottom:24px;">'
        '<div style="color:#C7D2FE; font-size:11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:6px;">Level 2 · AI Model Security</div>'
        '<div style="color:#fff; font-size:15px; margin-bottom:10px;"><strong>Guiding Question:</strong> How do we verify that the AI model we are deploying is actually what we think it is?</div>'
        '<div style="display:flex; gap:24px; flex-wrap:wrap; margin-top:12px;">'
        '<div><div style="color:#C7D2FE; font-size:11px; font-weight:600; margin-bottom:4px;">HEADLINE TOOLS</div>'
        '<div style="color:#fff; font-size:13px;">Picklescan · safetensors · Hugging Face Model Scanner · GitHub</div></div>'
        '<div><div style="color:#C7D2FE; font-size:11px; font-weight:600; margin-bottom:4px;">ROLES UNLOCKED</div>'
        '<div style="color:#fff; font-size:13px;">MLOps Security Engineer · AI Supply Chain Analyst · Junior MLSecOps Engineer</div></div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    # Hero header
    st.markdown(
        '<div style="background:linear-gradient(135deg, #1E1B4B 0%, #312E81 100%); padding:18px 32px; border-radius:8px; display:flex; justify-content:space-between; align-items:center; margin-bottom:28px;">'
        '<div style="color:#fff; font-size:22px; font-weight:700;">DataForge ML</div>'
        '<div style="color:#C7D2FE; font-size:13px;">Researcher Login &nbsp;&nbsp;&nbsp;&nbsp; Pipeline Docs</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(
            '<div style="font-size:32px; font-weight:800; color:#0F172A; line-height:1.3;">Genomics intelligence,<br>model integrity unknown.</div>'
            '<div style="font-size:14px; color:#475569; margin-top:12px; max-width:420px;">An intentionally vulnerable BioTech AI pipeline. Your job is to inspect the deployment code, audit the model source, run a live integrity scan, and harden the pipeline before a compromised model reaches production.</div>',
            unsafe_allow_html=True,
        )
        with st.expander("📋 View Scenario Brief"):
            st.markdown(
                "**The Company**\n\nDataForge ML supplies pre-trained genomics analysis models to healthcare research companies. "
                "They download open-source foundation models from public Hugging Face repositories, fine-tune them on proprietary biological datasets, and deploy them to client pipelines.\n\n"
                "**What Happened**\n\nThe team pulled a model weight file from an unverified Hugging Face user account without running any integrity checks. "
                "The model file uses the legacy pickle serialisation format, which can execute arbitrary code at load time. "
                "The downloaded model contains a hidden payload that executes when the model is loaded — giving an attacker persistent access to the genomics pipeline.\n\n"
                "**Your Three Tasks**\n\n"
                "1. Inspect the deployment code and the source model repository — identify what is wrong.\n"
                "2. Run Picklescan yourself in your Codespace terminal against the model fixture file in the repo.\n"
                "3. Fix `model_loader.py` by replacing pickle with safetensors and adding automated pre-load scanning."
            )
    with col2:
        st.markdown(ILLUSTRATION_DATAFORGE, unsafe_allow_html=True)

    st.markdown("---")

    # Section 1: Deployment Repository
    st.markdown("#### Deployment Repository")
    st.caption("The following files were found in the DataForge ML GitHub repository.")
    tab1, tab2, tab3 = st.tabs(["model_loader.py", "requirements.txt", "model_loader_hardened.py"])
    with tab1:
        st.code(
            '# model_loader.py\n'
            '# DataForge ML — Genomics Analysis Pipeline\n'
            '# AI model integration layer\n'
            '# Maintained by: ml-team@dataforge.io\n\n'
            'import pickle\n'
            'import requests\n'
            'from pathlib import Path\n\n'
            'MODEL_REPO = "logix-community/genomics-analyzer-v2"\n'
            'MODEL_FILE = "genomics_analyzer_v2.pkl"\n'
            'MODEL_URL  = f"https://huggingface.co/{MODEL_REPO}/resolve/main/{MODEL_FILE}"\n'
            'MODEL_PATH = Path("/tmp") / MODEL_FILE\n\n'
            'def download_model():\n'
            '    """Download model weights from Hugging Face."""\n'
            '    if not MODEL_PATH.exists():\n'
            '        print(f"Downloading {MODEL_FILE}...")\n'
            '        response = requests.get(MODEL_URL, stream=True)\n'
            '        with open(MODEL_PATH, "wb") as f:\n'
            '            for chunk in response.iter_content(chunk_size=8192):\n'
            '                f.write(chunk)\n'
            '    return MODEL_PATH\n\n'
            'def load_model():\n'
            '    """Load the genomics analysis model."""\n'
            '    model_path = download_model()\n'
            '    with open(model_path, "rb") as f:\n'
            '        model = pickle.load(f)\n'
            '    return model\n\n'
            'def analyze_sample(sample_data: dict) -> dict:\n'
            '    """Run genomics analysis on a patient sample."""\n'
            '    model = load_model()\n'
            '    results = model.predict(sample_data)\n'
            '    return {"status": "complete", "results": results}',
            language="python",
        )
    with tab2:
        st.code(
            'numpy==1.24.3\npandas==2.0.1\nscikit-learn==1.3.0\n'
            'requests==2.31.0\nhuggingface-hub==0.16.4\nbiopython==1.81\ntorch==2.0.1',
            language="text",
        )
    with tab3:
        st.caption("This is your workspace. Open levels/level2_dataforge.py in your forked Codespace and replace this placeholder with your hardened version.")
        st.code(
            '# model_loader_hardened.py\n'
            '# DataForge ML — Genomics Analysis Pipeline\n'
            '#\n'
            '# This is your workspace.\n'
            '# Open levels/level2_dataforge.py in your forked Codespace.\n'
            '# Replace this placeholder with your hardened version of model_loader.py.\n'
            '# Your commit showing this change is your Level 2 portfolio evidence.',
            language="python",
        )

    st.markdown("---")

    # Section 2: HF Repo Viewer
    st.markdown("#### Source Model Repository")
    st.caption("This is the Hugging Face repository the model was downloaded from. Audit it before reading any further.")
    render_hf_repo(user.email)

    st.markdown("---")

    # Section 3: Live Picklescan — student runs it themselves
    st.markdown("#### Model Integrity Scanner — Run This Yourself")
    st.info(
        "The model fixture file is already in your forked repo at `models/genomics_analyzer_v2.pkl`. "
        "Open your Codespace, run the commands below in the terminal, and record your findings. "
        "Do not skip this — your scan output is evidence in your Model Security Assessment."
    )

    st.markdown("**Step 1 — Install Picklescan:**")
    st.code("pip install picklescan", language="bash")

    st.markdown("**Step 2 — Run the scan against the fixture file:**")
    st.code("picklescan -p models/genomics_analyzer_v2.pkl", language="bash")

    st.markdown("**Step 3 — Interpret your output. You are looking for four things:**")
    st.markdown(
        "- **Infected files** — how many files contain threats\n"
        "- **Dangerous globals** — the specific dangerous import or callable detected\n"
        "- **The threat type** — what kind of payload is embedded (REDUCE opcode, subprocess, os, etc.)\n"
        "- **The verdict** — FOUND means the file is unsafe to load in any environment"
    )

    st.markdown("**What Picklescan is doing:**")
    st.markdown(
        "Picklescan performs static analysis — it reads the raw bytes of the pickle file and inspects "
        "the serialisation opcodes without executing any code. This is why it is safe to run against "
        "a malicious file. In production pipelines, Picklescan runs automatically inside the CI/CD "
        "pipeline before any model reaches the inference server — the manual run you are doing now "
        "teaches you what that automated check is doing and how to configure it yourself."
    )

    st.markdown("---")

    # Section 4: Model Threat Assessment
    st.markdown("#### Model Threat Assessment")
    st.caption("Based on your Picklescan output, complete this structured risk assessment. This is your DataForge ML deliverable.")

    st.markdown(
        '<div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:20px; margin-top:12px;">'
        '<div style="font-size:13px; font-weight:600; color:#1E293B; margin-bottom:16px;">DataForge ML — Model Security Assessment Template</div>'
        '<table style="width:100%; border-collapse:collapse; font-size:13px;">'
        '<thead><tr style="background:#F1F5F9;">'
        '<th style="padding:10px 14px; text-align:left; color:#64748B; border-bottom:1px solid #E2E8F0; width:35%;">Field</th>'
        '<th style="padding:10px 14px; text-align:left; color:#64748B; border-bottom:1px solid #E2E8F0;">Your Finding</th>'
        '</tr></thead><tbody>'
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px; color:#374151; font-weight:500;">Model File</td><td style="padding:10px 14px; color:#6B7280;"></td></tr>'
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px; color:#374151; font-weight:500;">Source Repository</td><td style="padding:10px 14px; color:#6B7280;"></td></tr>'
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px; color:#374151; font-weight:500;">Serialisation Format</td><td style="padding:10px 14px; color:#6B7280;"></td></tr>'
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px; color:#374151; font-weight:500;">Threats Detected</td><td style="padding:10px 14px; color:#6B7280;"></td></tr>'
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px; color:#374151; font-weight:500;">Threat Type</td><td style="padding:10px 14px; color:#6B7280;"></td></tr>'
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px; color:#374151; font-weight:500;">Threat Classification</td><td style="padding:10px 14px; color:#6B7280;"></td></tr>'
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px; color:#374151; font-weight:500;">Supply Chain Risk Factors</td><td style="padding:10px 14px; color:#6B7280;"></td></tr>'
        '<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:10px 14px; color:#374151; font-weight:500;">Business Impact</td><td style="padding:10px 14px; color:#6B7280;"></td></tr>'
        '<tr><td style="padding:10px 14px; color:#374151; font-weight:500;">Remediation Plan</td><td style="padding:10px 14px; color:#6B7280;"></td></tr>'
        '</tbody></table>'
        '<div style="margin-top:12px; font-size:11px; color:#94A3B8;">Complete this in a Google Doc, GitHub Gist, or Markdown file. You will paste the link below when submitting.</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Interview questions
    with st.expander("📋 Interview Questions for This Level"):
        st.markdown(
            "1. What is model supply chain poisoning and how would you detect it before deployment?\n"
            "2. What is the difference between loading a model with pickle vs safetensors?\n"
            "3. How would you build an automated pre-deployment model validation pipeline?\n"
            "4. What would you check on a Hugging Face model repo before pulling weights into production?\n"
            "5. Where in a CI/CD pipeline would you place Picklescan and why?"
        )

    st.markdown("---")

    # Submit section
    st.markdown("#### Submit Your Level 2 Work")

    if st.session_state.get("l2_completed"):
        st.success("✅ Level 2 is complete. Level 3 — CartBot AI is now unlocked.")
        if st.button("← Return to Hub", key="l2_return_done"):
            st.session_state.view = "hub"
            st.rerun()
        return

    st.info(
        "Before submitting, confirm you have completed all three tasks:\n\n"
        "1. **Identified the vulnerabilities** in model_loader.py and the source model repo.\n"
        "2. **Run Picklescan yourself** in your Codespace terminal and recorded the output.\n"
        "3. **Fixed model_loader.py** — replaced pickle with safetensors and added automated scanning.\n"
        "4. **Completed your Model Threat Assessment** document."
    )

    commit_url = st.text_input(
        "GitHub commit URL showing your model_loader.py fix:",
        placeholder="https://github.com/your-username/ai-security-defense-lab/commit/abc123",
        key="l2_commit_url",
    )
    report_url = st.text_input(
        "Model Threat Assessment link (Google Doc, GitHub Gist, or Markdown file):",
        placeholder="https://gist.github.com/your-username/...",
        key="l2_report_url",
    )

    if st.button("Submit Level 2 Work →", key="l2_submit"):
        if not commit_url or not report_url:
            st.warning("Paste both links above before submitting.")
        elif "github.com" not in commit_url and "gitlab.com" not in commit_url:
            st.warning("The first link must be a GitHub or GitLab commit URL.")
        else:
            try:
                supabase_client.table("defense_lab_progress").update({
                    "completed": True,
                    "completed_at": "now()",
                }).eq("user_id", str(user.id)).eq("level_number", 2).execute()
                st.session_state.l2_completed = True
                st.rerun()
            except Exception as e:
                st.error(f"Could not save progress: {e}")
