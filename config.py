import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if API key is loaded correctly
if not OPENAI_API_KEY:
    raise ValueError(" ERROR: OPENAI_API_KEY is missing! Please check your .env file.")

# Configuration Dictionary
CONFIG = {
    "OPENAI_API_KEY": OPENAI_API_KEY,
    "MODEL_NAME": "google/gemma-7b",  # Pre-trained model for Hinglish
}

# Debugging (Remove this after testing)
print(f" Loaded API Key: {OPENAI_API_KEY[:5]}********")
