"""
4_Chat_with_PDF.py

This page lets the student upload a PDF once, and then ask multiple
questions about it in a chat-style interface.
"""

import streamlit as st
from pdf_helper import extract_text_from_pdf, is_pdf_readable
from gemini_helper import ask_gemini

st.set_page_config(page_title="Chat with PDF - Study Buddy", page_icon="💬")

st.title("💬 Chat with PDF")
st.caption("Powered by Study Buddy — your AI study companion")
st.write("Upload a PDF, then ask questions about its content.")

# We use Streamlit's "session state" to remember things between reruns,
# since Streamlit re-runs the whole script every time you interact with it.
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # list of (role, message) tuples

# File uploader
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None and st.session_state.pdf_text is None:
    with st.spinner("Reading your PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    if is_pdf_readable(pdf_text):
        # Save the PDF text so we don't have to re-read it on every question
        st.session_state.pdf_text = pdf_text[:15000]  # trimmed for simplicity
        st.success("PDF loaded! You can start asking questions below.")
    else:
        st.error("We couldn't read any text from this PDF.")

st.markdown("---")

# Only show the chat once a PDF has been loaded
if st.session_state.pdf_text:

    # Display the past conversation
    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(message)

    # Chat input box (stays fixed at the bottom of the page)
    user_question = st.chat_input("Ask a question about your PDF...")

    if user_question:
        # Show the student's question immediately
        with st.chat_message("user"):
            st.write(user_question)
        st.session_state.chat_history.append(("user", user_question))

        # Build a prompt that includes the PDF content as context
        prompt = f"""
You are a helpful study assistant. Answer the student's question using
ONLY the information in the document below. If the answer isn't in the
document, say so honestly.

Document:
\"\"\"{st.session_state.pdf_text}\"\"\"

Student's question: {user_question}
"""
        with st.spinner("Thinking..."):
            answer = ask_gemini(prompt)

        with st.chat_message("assistant"):
            st.write(answer)
        st.session_state.chat_history.append(("assistant", answer))

else:
    st.info("📎 Please upload a PDF above to start chatting.")
