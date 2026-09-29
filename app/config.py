import os
from dotenv import load_dotenv

load_dotenv()

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")

HINDSIGHT_BASE_URL = os.getenv(
    "HINDSIGHT_BASE_URL",
    "https://api.hindsight.vectorize.io"
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

LLM_MODEL = os.getenv("LLM_MODEL", "openai/gpt-oss-120b")
FALLBACK_MODEL = os.getenv("FALLBACK_MODEL", "openai/gpt-oss-20b")

BANK_ID = os.getenv(
    "BANK_ID",
    "incidentmind-team"
)
