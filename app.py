import os
import threading
os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Load custom CSS for styling
def load_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.cache_resource

def load_crew():
    from crew import legal_assistant_crew
    return legal_assistant_crew

threading.Thread(target=load_crew, daemon=True).start()

st.set_page_config(page_title="Smart Legal Assistant", page_icon="🧠", layout="wide")
load_css("style.css")

# Header Section
st.markdown("""
<div class="legal-header">
    <div class="badge">⚖ AI-Powered Legal Intelligence</div>
    <h1>Smart <span>Legal</span> Assistant</h1>
    <p>Describe your legal problem in plain English and receive structured analysis powered by intelligent agents.</p>
    <div class="pills">
        <span class="pill">📋 Case Analysis</span>
        <span class="pill">📖 IPC Sections</span>
        <span class="pill">🔍 Case Retrieval</span>
    </div>
</div>
""", unsafe_allow_html=True)


# Input Section
col1, col2, col3 = st.columns([1, 2.4, 1])

with col2:
    st.markdown('<div class="card"><div class="card-title">📝 Describe Your Legal Issue</div>', unsafe_allow_html=True)

    with st.form("legal_form"):
        user_input = st.text_area(
            label="",
            placeholder="e.g. My landlord is refusing to return my security deposit after I vacated the property 2 months ago...",
            height=220,
        )
        submitted = st.form_submit_button("⚖️   Run Legal Assistant")

    st.markdown('</div>', unsafe_allow_html=True)

    if submitted:
        if not user_input.strip():
            st.warning("⚠️  Please describe your legal issue before submitting.")
        else:
            with st.spinner("🔍  Analyzing your case — this may take a moment..."):
                crew = load_crew()
                result = crew.kickoff(inputs={"user_input": user_input})

            st.success("✅  Analysis complete.")
            st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-title" style="margin-bottom:0.5rem;">📄 Legal Analysis Report</div>', unsafe_allow_html=True)

            output_text = result if isinstance(result, str) else str(result)
            st.markdown(f'<div class="result-card">{output_text}</div>', unsafe_allow_html=True)



# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="legal-footer">
    Smart Legal Assistant &nbsp;·&nbsp; For informational purposes only &nbsp;·&nbsp; Not a substitute for professional legal advice
</div>
""", unsafe_allow_html=True)        