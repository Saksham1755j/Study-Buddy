"""
pdf_helper.py

This file handles everything related to reading PDF files.
It is used by two pages: PDF Summarizer and Chat with PDF.

Why keep this separate?
- Both pages need the same "read text from a PDF" logic
- Instead of copying the same code twice, we write it once here and reuse it
"""

from PyPDF2 import PdfReader


def extract_text_from_pdf(uploaded_file):
    """
    Takes an uploaded PDF file (from Streamlit's file_uploader) and
    returns all the text found inside it as one big string.

    Parameters:
        uploaded_file: the file object Streamlit gives us after upload

    Returns:
        str: all extracted text from the PDF (empty string if none found)
    """
    try:
        reader = PdfReader(uploaded_file)
        full_text = ""

        # Loop through every page in the PDF and collect its text
        for page in reader.pages:
            page_text = page.extract_text()

            # Some pages (like scanned images) may return None, so we check first
            if page_text:
                full_text += page_text + "\n"

        return full_text

    except Exception as error:
        # Beginner-friendly error handling
        print(f"⚠️ Error reading PDF: {error}")
        return ""


def is_pdf_readable(extracted_text):
    """
    Simple check to see if we actually got usable text out of the PDF.
    Useful for showing a warning if someone uploads a scanned/image-only PDF.

    Parameters:
        extracted_text (str): the text returned by extract_text_from_pdf()

    Returns:
        bool: True if there is enough real text to work with
    """
    # If the PDF is empty or has very little text, treat it as "not readable"
    return len(extracted_text.strip()) > 20
