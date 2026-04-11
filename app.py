import os
import threading
os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

@st.cache_resource

def load_crew():
    from crew import legal_assistant_crew
    return legal_assistant_crew

threading.Thread(target=load_crew, daemon=True).start()

st.set_page_config(page_title="Smart Legal Assistant", page_icon="🧠", layout="wide")

st.title("⚖️ SMART LEGAL ASSISTANT")
st.markdown(
    "Enter a legal problem in plain English. This assistant will help you:\n"
    "- Understand the legal issue\n"
    "- Find applicable IPC sections\n"
    "- Retrieve matching precedent cases\n"
)
with st.form("legal_form"):
    user_input = st.text_area("Deacribe Your Legal issue:", height=250)
    submitted = st.form_submit_button("🔍 Run Legal Assistant")

if submitted:
    if not user_input.strip():
        st.warning("Empty Input!!! Please enter a legal issue to analyze.")
    else:
        with st.spinner("🔎 Analyzing your case"):
            crew = load_crew()
            result = crew.kickoff(inputs={"user_input": user_input})

        st.success("Assistant completed the workflow!")

        st.subheader("Final Output")
        st.markdown(result if isinstance(result, str) else str(result))
        