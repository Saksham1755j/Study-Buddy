# 📚 Study Buddy

Study Buddy is a simple AI-powered study assistant built with **Python**,
**Streamlit**, and the **Google Gemini API**. It was built as a college
internship project.

## Features

1. **Home Page** - Welcome message, logo, and feature overview
2. **AI Tutor** - Ask any question and get a simple explanation
3. **PDF Summarizer** - Upload a PDF and get a summary with key points
4. **Quiz Generator** - Generate 5 or 10 MCQs from a topic or a PDF
5. **Chat with PDF** - Upload a PDF and ask follow-up questions about it

## Technology Used

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web app framework / user interface |
| Google Gemini API (`google-genai`) | AI model that powers all features |
| PyPDF2 | Extracting text from uploaded PDF files |
| python-dotenv | Loading the API key from a `.env` file |

## Project Structure

```
Study_Buddy/
├── app.py                     # Home page - runs the whole app
├── assets/
│   └── logo.png                # App logo
├── pages/
│   ├── 1_AI_Tutor.py
│   ├── 2_PDF_Summarizer.py
│   ├── 3_Quiz_Generator.py
│   └── 4_Chat_with_PDF.py
├── utils/
│   ├── gemini_helper.py        # All Gemini API calls
│   ├── pdf_helper.py           # PDF text extraction
│   └── quiz_helper.py          # Quiz prompt building + parsing
├── .streamlit/
│   └── config.toml             # Purple theme settings
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## How to Run This Project

### 1. Install Python
Make sure Python 3.10+ is installed on your computer.

### 2. Open a terminal in the project folder
```bash
cd Study_Buddy
```

### 3. (Recommended) Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 4. Install the required packages
```bash
pip install -r requirements.txt
```

### 5. Add your Gemini API key
1. Copy `.env.example` and rename the copy to `.env`
2. Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey)
3. Paste it into `.env` like this:
   ```
   GEMINI_API_KEY=your_real_key_here
   ```

### 6. Run the app
```bash
streamlit run app.py
```

The app will open automatically in your browser (usually at `http://localhost:8501`).

## How Each Feature Works (Quick Explanation)

- **AI Tutor**: Takes the student's typed question, wraps it in a "explain
  simply" prompt, and sends it to Gemini via `ask_gemini()`.
- **PDF Summarizer**: Extracts text from the uploaded PDF using `PyPDF2`,
  then asks Gemini to summarize it and list key points.
- **Quiz Generator**: Asks Gemini to generate MCQs in a strict text format,
  then uses a regular expression in `quiz_helper.py` to turn that text into
  structured question/option/answer data for display.
- **Chat with PDF**: Extracts the PDF text once and stores it in Streamlit's
  `session_state`. Every question the student asks is sent to Gemini along
  with the PDF text as context, so the AI can answer based on the document.

## Notes

- This is a beginner-friendly student project, not a production application.
- PDF text is trimmed to a reasonable length before being sent to Gemini,
  to keep the app simple, fast, and easy to explain.
- All AI calls go through one central file (`utils/gemini_helper.py`) so
  the logic is easy to find and explain during a viva.
