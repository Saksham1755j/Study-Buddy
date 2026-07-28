"""
2_PDF_Summarizer.py

This page lets the student upload a PDF and get:
1. A short summary
2. A list of key points
"""

import streamlit as st
from pdf_helper import extract_text_from_pdf, is_pdf_readable
from gemini_helper import ask_gemini

st.set_page_config(page_title="PDF Summarizer - Study Buddy", page_icon="📄")

st.title("📄 PDF Summarizer")
st.caption("Powered by Study Buddy — your AI study companion")
st.write("Upload a PDF and get a simple summary with key points.")

# File uploader - only accepts PDF files
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Reading your PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    # Check the PDF actually had readable text (not just scanned images)
    if not is_pdf_readable(pdf_text):
        st.error(
            "We couldn't read any text from this PDF. "
            "It might be a scanned/image-only file."
        )
    else:
        st.success("PDF loaded successfully!")

        if st.button("✨ Generate Summary"):
            with st.spinner("Summarizing..."):
                # Gemini has a large context window, but we still trim very
                # long PDFs to keep the app simple and fast for a student project
                trimmed_text = pdf_text[:15000]

                prompt = f"""
You are a helpful study assistant. Read the following document text and:

1. Write a short summary (around 150 words)
2. List 5-7 key points as a simple bullet list

Document text:
\"\"\"{trimmed_text}\"\"\"
"""
                summary = ask_gemini(prompt)

            st.markdown("### 📋 Summary & Key Points")
            st.write(summary)
