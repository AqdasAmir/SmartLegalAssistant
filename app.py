
import streamlit as st
from dotenv import load_dotenv
from crew import legal_assistant_crew

load_dotenv()

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
            result = legal_assistant_crew.kickoff(inputs={"user_input": user_input})

        st.success("Assistant completed the workflow!")

        st.subheader("Final Output")
        st.markdown(result if isinstance(result, str) else str(result))
        