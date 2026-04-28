import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_resume(resume_text, job_description):
    """
    Sends resume and job description to GPT-4o.
    Returns a structured analysis as a Python dictionary.
    """

    prompt = f"""
You are an expert career coach and ATS (Applicant Tracking System) specialist.

Analyze the following resume against the job description and return ONLY a JSON object with this exact structure:

{{
  "match_score": <integer between 0 and 100>,
  "matched_skills": [<list of skills from resume that match job description>],
  "missing_skills": [<list of important skills in job description but missing from resume>],
  "suggestions": [<list of 3-5 specific actionable suggestions to improve the resume>],
  "summary": "<2-3 sentence overall summary of the candidate's fit>"
}}

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return ONLY the JSON. No explanation, no markdown, no extra text.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional resume analyzer. Always respond with valid JSON only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1000
    )

    result_text = response.choices[0].message.content.strip()

    try:
        result = json.loads(result_text)
    except json.JSONDecodeError:
        # If GPT adds extra text, extract JSON from it
        start = result_text.find("{")
        end = result_text.rfind("}") + 1
        result = json.loads(result_text[start:end])

    return result
