import streamlit as st

ILLUSTRATION_DATAFORGE = '<svg viewBox="0 0 320 240" width="100%" height="220"><circle cx="160" cy="120" r="110" fill="#EEF2FF"/><rect x="85" y="60" width="90" height="110" rx="6" fill="#1E1B4B"/><rect x="85" y="60" width="90" height="18" rx="6" fill="#312E81"/><rect x="93" y="88" width="74" height="6" rx="2" fill="#6366F1" opacity="0.6"/><rect x="93" y="100" width="60" height="6" rx="2" fill="#6366F1" opacity="0.6"/><rect x="93" y="112" width="68" height="6" rx="2" fill="#6366F1" opacity="0.6"/><rect x="93" y="124" width="50" height="6" rx="2" fill="#6366F1" opacity="0.6"/><rect x="93" y="136" width="64" height="6" rx="2" fill="#EF4444" opacity="0.8"/><rect x="93" y="148" width="44" height="6" rx="2" fill="#EF4444" opacity="0.8"/><circle cx="207" cy="85" r="28" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/><text x="207" y="91" font-size="22" text-anchor="middle" fill="#EF4444">!</text><line x1="175" y1="100" x2="185" y2="90" stroke="#EF4444" stroke-width="2" stroke-dasharray="3,2"/><line x1="155" y1="130" x2="155" y2="165" stroke="#6366F1" stroke-width="1.5" opacity="0.5"/><line x1="185" y1="130" x2="185" y2="165" stroke="#6366F1" stroke-width="1.5" opacity="0.5"/><path d="M155,145 C162,138 178,138 185,145" fill="none" stroke="#A5B4FC" stroke-width="1.5"/><path d="M155,155 C162,162 178,162 185,155" fill="none" stroke="#A5B4FC" stroke-width="1.5"/><circle cx="155" cy="145" r="3" fill="#6366F1"/><circle cx="185" cy="145" r="3" fill="#6366F1"/><circle cx="155" cy="155" r="3" fill="#6366F1"/><circle cx="185" cy="155" r="3" fill="#6366F1"/><circle cx="245" cy="155" r="11" fill="#F1C9A6"/><rect x="233" y="166" width="22" height="30" rx="5" fill="#4F46E5"/><circle cx="275" cy="160" r="10" fill="#E8B589"/><rect x="264" y="170" width="22" height="26" rx="5" fill="#818CF8"/></svg>'

SCAN_OUTPUT = (
    "Scanning: /models/genomics_analyzer_v2.pkl\n"
    "──────────────────────────────────────────────────────────────\n"
    "[SCAN] Loading model file: genomics_analyzer_v2.pkl (487.3 MB)\n"
    "[SCAN] Checking serialisation format... pickle detected\n"
    "[SCAN] Extracting opcodes...\n"
    "[SCAN] Analysing imported modules...\n"
    "\n"
    "  ⚠  THREAT DETECTED — CRITICAL\n"
    "     Type:     REDUCE opcode with custom __reduce__ method\n"
    "     Location: byte offset 0x3F2A1B\n"
    "     Detail:   Object reconstruction override enables arbitrary\n"
    "               code execution at model load time\n"
    "\n"
    "  ⚠  THREAT DETECTED — HIGH\n"
    "     Type:     Unsafe module import — subprocess\n"
    "     Location: byte offset 0x3F2B44\n"
    "     Detail:   subprocess imported inside serialised object.\n"
    "               Enables shell command execution on the host\n"
    "\n"
    "  ⚠  THREAT DETECTED — HIGH\n"
    "     Type:     Encoded executable sequence\n"
    "     Location: byte offset 0x3F3C11\n"
    "     Detail:   Base64-encoded payload detected in weight tensor.\n"
    "               Pattern consistent with reverse shell or\n"
    "               data exfiltration code\n"
    "\n"
    "──────────────────────────────────────────────────────────────\n"
    "SCAN COMPLETE\n"
    "  Threats found:    3 (1 CRITICAL, 2 HIGH)\n"
    "  Model status:     UNSAFE — DO NOT LOAD IN ANY ENVIRONMENT\n"
    "  Recommendation:   Source a verified model from a trusted\n"
    "                    account and convert to safetensors format\n"
    "\n"
    "Picklescan v0.0.14 · https://github.com/mmaitre314/picklescan"
)

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
            '<div style="font-size:14px; color:#475569; margin-top:12px; max-width:420px;">An intentionally vulnerable BioTech AI pipeline. Your job is to inspect the deployment code, audit the model source, scan the weights, and harden the pipeline before a compromised model reaches production.</div>'
            '<div style="margin-top:18px;">'
            '<span style="background:#6366F1; color:#fff; padding:10px 22px; border-radius:6px; font-weight:600; font-size:14px; margin-right:12px; display:inline-block;">Begin Audit</span>'
            '<span style="border:1px solid #94A3B8; color:#475569; padding:10px 22px; border-radius:6px; font-weight:500; font-size:14px; display:inline-block;">View Brief</span>'
            '</div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(ILLUSTRATION_DATAFORGE, unsafe_allow_html=True)

    st.markdown("---")

    # Section 1: Deployment Repository
    st.markdown("#### Deployment Repository")
    st.caption("The following files were found in the DataForge ML GitHub repository.")
    tab1, tab2 = st.tabs(["model_loader.py", "requirements.txt"])
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
            'numpy==1.24.3\n'
            'pandas==2.0.1\n'
            'scikit-learn==1.3.0\n'
            'requests==2.31.0\n'
            'huggingface-hub==0.16.4\n'
            'biopython==1.81\n'
            'torch==2.0.1',
            language="text",
        )

    st.markdown("---")

    # Section 2: HF Repo Viewer
    st.markdown("#### Source Model Repository")
    st.caption("This is the Hugging Face repository the model was downloaded from.")
    render_hf_repo(user.email)

    st.markdown("---")

    # Section 3: Picklescan
    st.markdown("#### Model Integrity Scanner")
    st.caption("Run an integrity scan against the downloaded model weight file before loading it into any environment.")

    if not st.session_state.get("l2_scan_run"):
        if st.button("▶ Run Picklescan on genomics_analyzer_v2.pkl", key="run_scan"):
            st.session_state.l2_scan_run = True
            st.rerun()
    else:
        st.code(SCAN_OUTPUT, language="bash")

    st.markdown("---")

    # Interview questions
    with st.expander("📋 Interview Questions for This Level"):
        st.markdown(
            "1. What is model supply chain poisoning and how would you detect it before deployment?\n"
            "2. What is the difference between loading a model with pickle vs safetensors?\n"
            "3. How would you build an automated pre-deployment model validation pipeline?\n"
            "4. What would you check on a Hugging Face model repo before pulling weights into production?"
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
        "2. **Replaced pickle.load** with safetensors and added a pre-load Picklescan check to the pipeline.\n"
        "3. **Written your Model Security Incident Report** documenting the compromised model and the fix."
    )

    commit_url = st.text_input(
        "GitHub commit URL showing your model_loader.py fix:",
        placeholder="https://github.com/your-username/ai-security-defense-lab/commit/abc123",
        key="l2_commit_url",
    )
    report_url = st.text_input(
        "Model Security Incident Report link (GitHub Gist, Google Doc, or Medium post):",
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
