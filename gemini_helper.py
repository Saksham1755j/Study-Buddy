"""
gemini_helper.py

This is the ONLY file that talks directly to the Gemini AI model.
Every page in the app (AI Tutor, PDF Summarizer, Quiz Generator, Chat with PDF)
calls the functions in this file instead of calling Gemini directly.

Why do it this way?
- Keeps our AI code in one place, so it's easy to find and explain
- If Google ever changes the SDK, we only need to update this ONE file
"""

import os
from dotenv import load_dotenv
from google import genai

# Load the variables from our .env file (like GEMINI_API_KEY) into the environment
load_dotenv()

# The Gemini model we are using for this project.
# "gemini-flash-latest" is an ALIAS that always points to Google's current
# best Flash model. We use this instead of pinning to one exact model name
# (like "gemini-2.5-flash") because Google regularly retires older model
# versions - using the alias means our project keeps working without
# needing code changes every time that happens.
MODEL_NAME = "gemini-flash-latest"


def get_gemini_client():
    """
    Creates and returns a Gemini client using our API key.
    This client is what we use to send prompts to the AI model.
    """
    api_key = os.getenv("GEMINI_API_KEY")

    # Basic error handling: check the key was actually loaded
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found. Make sure you created a .env file "
            "with your API key (see .env.example)."
        )

    client = genai.Client(api_key=api_key)
    return client


def ask_gemini(prompt):
    """
    Sends a text prompt to Gemini and returns the AI's text response.
    This is the main function used by almost every page in the app.

    Parameters:
        prompt (str): The question or instruction we want the AI to respond to

    Returns:
        str: The AI's reply as plain text
    """
    try:
        client = get_gemini_client()

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text

    except Exception as error:
        # Beginner-friendly error handling: show a simple message instead of crashing
        return f"⚠️ Something went wrong while contacting Gemini: {error}"
