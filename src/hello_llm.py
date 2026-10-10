import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

SYSTEM = (
    "You are a maintenance assistant for factory equipment. "
    "Answer in 3 short bullet points. If you are unsure, say so."
)


def ask(question: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM,
            max_output_tokens=50,
        ),
    )
    usage = response.usage_metadata
    print(f"[tokens] in={usage.prompt_token_count} out={usage.candidates_token_count}")
    return response.text


if __name__ == "__main__":
    print(ask("A conveyor motor is overheating. What should I check first?"))