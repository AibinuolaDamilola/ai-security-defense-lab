import streamlit as st


def render_level2(user, supabase_client):
    st.markdown(
        '<div style="background:linear-gradient(135deg, #1E1B4B, #312E81); border-radius:10px; padding:20px 28px; margin-bottom:24px;">'
        '<div style="color:#C7D2FE; font-size:11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:6px;">Level 2 · AI Model Security</div>'
        '<div style="color:#fff; font-size:15px;"><strong>Guiding Question:</strong> How do we verify that the AI model we are deploying is actually what we think it is?</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.markdown("## DataForge ML — BioTech Model Security Lab")
    st.info("🔬 This level is under active development and will be available soon. Complete Level 1 to be first notified when Level 2 launches.")
    st.markdown("**What you will learn in Level 2:**")
    st.markdown(
        "- AI model supply chain attacks and how they happen\n"
        "- How to inspect a Hugging Face model repo for signs of compromise\n"
        "- Running Picklescan against model weight files\n"
        "- Replacing unsafe pickle loading with safetensors\n"
        "- Writing an automated pre-deployment model validation pipeline"
    )
    st.markdown("**Roles unlocked after Level 2:** MLOps Security Engineer · AI Supply Chain Analyst · Junior MLSecOps Engineer")
