import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def explain_code(code):

    prompt = f"""
    Explain this code in plain English.

    Rules:
    - Keep it between 2 and 4 sentences.
    - Explain what the code does.
    - Mention important logic.
    - Mention time complexity if possible.
    - If uncertain, say so.
    - Do not hallucinate.

    Code:

    {code}
    """

    response = model.generate_content(prompt)

    return response.text


st.title("🤖 AI-Powered Code Explainer")

st.write(
    "Paste Python or JavaScript code and get a simple explanation."
)


language = st.selectbox(
    "Select Language",
    ["Python", "JavaScript"]
)


code = st.text_area(
    "Paste your code here",
    height=250
)


if "history" not in st.session_state:
    st.session_state.history = []


if st.button("Explain"):

    if code.strip():

        explanation = explain_code(code)

        st.session_state.history.append({

            "language": language,

            "code": code,

            "explanation": explanation

        })


st.header("Previous Explanations")


for item in reversed(st.session_state.history):

    st.subheader(item["language"])

    st.code(
        item["code"],
        language=item["language"].lower()
    )

    st.write(item["explanation"])

    st.divider()