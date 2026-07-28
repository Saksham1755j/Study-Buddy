"""
1_AI_Tutor.py

This page lets the student type any question and get a simple,
beginner-friendly explanation from Gemini.
"""

import streamlit as st
from gemini_helper import ask_gemini

st.set_page_config(page_title="AI Tutor - Study Buddy", page_icon="🤖")

st.title("🤖 AI Tutor")
st.caption("Powered by Study Buddy — your AI study companion")
st.write("Ask any question and get a simple, easy-to-understand explanation.")

# Text box for the student's question
user_question = st.text_area(
    "What do you want to learn about?",
    placeholder="e.g. Explain what a linked list is in simple terms"
)

# Button to trigger the AI call
if st.button("🚀 Ask AI Tutor"):
    if user_question.strip() == "":
        st.warning("Please type a question first.")
    else:
        with st.spinner("Thinking..."):
            # We ask Gemini to specifically explain things simply,
            # since this is a TUTOR feature for students
            prompt = f"""
You are a friendly and patient tutor. Explain the following question in
simple, easy-to-understand language, as if teaching a beginner student.
Use short paragraphs and simple examples where helpful.

Question: {user_question}
"""
            answer = ask_gemini(prompt)

        st.markdown("### 💡 Answer")
        st.write(answer)
