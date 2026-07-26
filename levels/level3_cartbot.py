import streamlit as st


def render_level3(user, supabase_client):
    st.markdown(
        '<div style="background:linear-gradient(135deg, #7C2D12, #9A3412); border-radius:10px; padding:20px 28px; margin-bottom:24px;">'
        '<div style="color:#FED7AA; font-size:11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:6px;">Level 3 · Application & API Security for AI</div>'
        '<div style="color:#fff; font-size:15px;"><strong>Guiding Question:</strong> How do we protect the interface between users and the AI model from being exploited?</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.markdown("## CartBot AI — E-Commerce API Security Lab")
    st.info("🛡️ This level is under active development and will be available soon. Complete Levels 1 and 2 to unlock.")
    st.markdown("**What you will learn in Level 3:**")
    st.markdown(
        "- How AI APIs differ from traditional APIs and where they break\n"
        "- API key authentication and rotation practices\n"
        "- Token-based rate limiting for LLM endpoints\n"
        "- Direct prompt injection at the API layer (OWASP LLM01 deep dive)\n"
        "- Output filtering and response sanitization"
    )
    st.markdown("**Roles unlocked after Level 3:** AI Application Security Engineer · Application Security Analyst · Junior Penetration Tester (AI)")
