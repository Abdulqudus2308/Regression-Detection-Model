import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

MODEL = "gemini-3.5-flash-lite"

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate(system_prompt, user_text):
    response = client.models.generate_content(
        model=MODEL,
        contents=user_text,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0,
            response_mime_type="application/json",
        ),
    )
    return response.text
