"""
3_Quiz_Generator.py

This page generates a multiple choice quiz (5 or 10 questions) either from:
- A topic the student types in, OR
- A PDF the student uploads
"""

import streamlit as st
from pdf_helper import extract_text_from_pdf, is_pdf_readable
from gemini_helper import ask_gemini
from quiz_helper import build_quiz_prompt, parse_quiz_response

st.set_page_config(page_title="Quiz Generator - Study Buddy", page_icon="📝")

st.title("📝 Quiz Generator")
st.caption("Powered by Study Buddy — your AI study companion")
st.write("Generate a multiple choice quiz from a topic or an uploaded PDF.")

# Let the student choose where the quiz content comes from
source_option = st.radio(
    "Generate quiz from:",
    ["Topic", "Uploaded PDF"]
)

quiz_content = None  # will hold either the topic text or PDF text

if source_option == "Topic":
    quiz_content = st.text_input(
        "Enter a topic",
        placeholder="e.g. Newton's Laws of Motion"
    )
else:
    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
    if uploaded_file is not None:
        with st.spinner("Reading your PDF..."):
            pdf_text = extract_text_from_pdf(uploaded_file)

        if is_pdf_readable(pdf_text):
            # Trim long PDFs to keep things simple and fast
            quiz_content = pdf_text[:15000]
            st.success("PDF loaded successfully!")
        else:
            st.error("We couldn't read any text from this PDF.")

# Let the student choose how many questions
num_questions = st.selectbox("Number of questions", [5, 10])

# Generate button
if st.button("🎯 Generate Quiz"):
    if not quiz_content or quiz_content.strip() == "":
        st.warning("Please enter a topic or upload a PDF first.")
    else:
        with st.spinner("Generating quiz..."):
            prompt = build_quiz_prompt(quiz_content, num_questions)
            raw_response = ask_gemini(prompt)
            quiz_questions = parse_quiz_response(raw_response)

        if len(quiz_questions) == 0:
            st.error("Sorry, we couldn't generate the quiz. Please try again.")
        else:
            st.markdown("### 🏆 Your Quiz")

            # Display each question with its options and a reveal-able answer
            for i, q in enumerate(quiz_questions, start=1):
                st.markdown(f"**Q{i}. {q['question']}**")

                option_letters = ["A", "B", "C", "D"]
                for letter, option_text in zip(option_letters, q["options"]):
                    st.write(f"{letter}) {option_text}")

                # Hide the answer until the student clicks to reveal it
                with st.expander("✅ Show Answer"):
                    st.write(f"Correct answer: **{q['answer']}**")

                st.markdown("---")
