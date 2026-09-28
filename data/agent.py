import os
from dotenv import load_dotenv
from hindsight_client import Hindsight
from groq import Groq

load_dotenv()

hindsight = Hindsight(
    api_key=os.getenv("HINDSIGHT_API_KEY"),
    base_url=os.getenv(
        "HINDSIGHT_BASE_URL",
        "https://api.hindsight.vectorize.io"
    )
)

groq = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_incident(incident):
    recalled = hindsight.recall(
        incident,
        limit=5
    )

    context = "\n".join(str(item) for item in recalled)

    prompt = f"""
You are IncidentMind, an AI incident-response assistant.

New incident:
{incident}

Relevant historical incidents:
{context}

Analyze the incident using the historical evidence.

Provide:
1. Likely root cause
2. Similar past incidents
3. Recommended next steps
4. Evidence supporting the recommendation
5. Risks or safety checks
6. Whether the recommendation should be verified by an engineer
"""

    response = groq.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
