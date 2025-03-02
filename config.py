import os
from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(" ERROR: OPENAI_API_KEY is missing! Please check your .env file.")

CONFIG = {
    "OPENAI_API_KEY": OPENAI_API_KEY,
    "MODEL_NAME": "google/gemma-2b-it",
}

