"""
app.py

This is the MAIN file of Study Buddy. Running this file starts the app:
    streamlit run app.py

This file is the HOME PAGE. It shows a welcome message, the app logo,
and feature cards explaining what the app can do.

Streamlit automatically turns every .py file inside the "pages/" folder
into a page in the sidebar menu - we don't need extra code for that.
"""

import streamlit as st

# ---- Basic page setup (must be the first Streamlit command) ----
st.set_page_config(
    page_title="Study Buddy",
    page_icon="📚",
    layout="wide"
)

# ---- Custom CSS for a modern, polished look ----
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Apply font globally */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Hero gradient banner */
    .hero-banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px;
        padding: 2.5rem 2rem;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .hero-banner h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: white !important;
    }
    .hero-banner p {
        font-size: 1.1rem;
        opacity: 0.92;
        max-width: 600px;
        margin: 0 auto;
        color: white !important;
    }

    /* Feature cards */
    .feature-card {
        background: white;
        border: 1px solid #e8e8ef;
        border-radius: 14px;
        padding: 1.5rem;
        text-align: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        height: 100%;
    }
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.15);
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 0.75rem;
    }
    .feature-card h3 {
        font-size: 1.1rem;
        font-weight: 600;
        color: #2d2d3f;
        margin-bottom: 0.5rem;
    }
    .feature-card p {
        font-size: 0.92rem;
        color: #6b7280;
        line-height: 1.5;
    }

    /* Footer tip bar */
    .tip-bar {
        background: linear-gradient(90deg, #eef2ff, #faf5ff);
        border: 1px solid #e0e7ff;
        border-radius: 12px;
        padding: 1rem 1.5rem;
        text-align: center;
        margin-top: 1.5rem;
        font-size: 0.95rem;
        color: #4338ca;
    }
</style>
""", unsafe_allow_html=True)

# ---- Sidebar ----
st.sidebar.title("📚 Study Buddy")
st.sidebar.write("Your personal AI-powered study companion.")
st.sidebar.markdown("---")
st.sidebar.write("👈 Choose a feature from the menu above.")

# ---- Hero Banner ----
st.markdown("""
<div class="hero-banner">
    <h1>📚 Study Buddy</h1>
    <p>Your AI-powered study companion — ask questions, summarize PDFs,
    generate quizzes, and chat with your notes.</p>
</div>
""", unsafe_allow_html=True)

# ---- Feature cards ----
st.subheader("✨ What can Study Buddy do?")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <h3>AI Tutor</h3>
        <p>Ask any question and get a simple, clear explanation instantly.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📄</div>
        <h3>PDF Summarizer</h3>
        <p>Upload a PDF and get a short summary with key points.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📝</div>
        <h3>Quiz Generator</h3>
        <p>Generate 5 or 10 MCQs from any topic or uploaded PDF.</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💬</div>
        <h3>Chat with PDF</h3>
        <p>Upload a PDF and ask questions directly about its content.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="tip-bar">
    💡 <strong>Tip:</strong> Use the sidebar on the left to get started with any feature!
</div>
""", unsafe_allow_html=True)
