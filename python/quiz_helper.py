"""
quiz_helper.py

This file handles everything related to building quizzes.
It is used by the Quiz Generator page.

Why keep this separate?
- Building the prompt and reading Gemini's answer back into a clean
  question/options/answer format is a bit fiddly - keeping it here
  keeps the page file itself short and easy to read
"""

import re


def build_quiz_prompt(content, num_questions):
    """
    Builds the instruction we send to Gemini to generate a quiz.
    We ask Gemini to follow an EXACT format so we can read the reply
    back into separate questions, options, and answers.

    Parameters:
        content (str): either a topic name (e.g. "Photosynthesis")
                        or text extracted from an uploaded PDF
        num_questions (int): how many questions to generate (5 or 10)

    Returns:
        str: the full prompt to send to Gemini
    """
    prompt = f"""
You are a helpful teacher creating a multiple choice quiz.

Create exactly {num_questions} multiple choice questions based on the
following content:

\"\"\"{content}\"\"\"

Follow this EXACT format for every question, with nothing extra before
or after it:

Q1: <question text>
A) <option A>
B) <option B>
C) <option C>
D) <option D>
ANSWER: <correct letter, just A or B or C or D>

Q2: <question text>
...continue the same pattern for all questions.
"""
    return prompt


def parse_quiz_response(raw_text):
    """
    Takes Gemini's raw text reply (in the format from build_quiz_prompt)
    and turns it into a list of dictionaries that are easy to display
    in Streamlit.

    Parameters:
        raw_text (str): Gemini's text response

    Returns:
        list of dict: each dict has 'question', 'options' (list of 4),
                       and 'answer' (the correct letter)
    """
    quiz_questions = []

    # This pattern looks for each question block one at a time
    pattern = re.compile(
        r"Q\d+:\s*(.*?)\s*"
        r"A\)\s*(.*?)\s*"
        r"B\)\s*(.*?)\s*"
        r"C\)\s*(.*?)\s*"
        r"D\)\s*(.*?)\s*"
        r"ANSWER:\s*([A-D])",
        re.DOTALL
    )

    matches = pattern.findall(raw_text)

    for match in matches:
        question_text, option_a, option_b, option_c, option_d, answer = match

        quiz_questions.append({
            "question": question_text.strip(),
            "options": [
                option_a.strip(),
                option_b.strip(),
                option_c.strip(),
                option_d.strip(),
            ],
            "answer": answer.strip()
        })

    return quiz_questions
