from groq import Groq

from app.config import (
    GROQ_API_KEY,
    LLM_MODEL,
    FALLBACK_MODEL,
)


def get_client():
    """Create and return the Groq client."""
    return Groq(api_key=GROQ_API_KEY)


def generate_response(prompt):
    """
    Generate an AI response using the primary model.
    If it fails, automatically try the fallback model.
    """

    client = get_client()

    models = [
        LLM_MODEL,
        FALLBACK_MODEL,
    ]

    last_error = None

    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are IncidentMind, an AI incident-response "
                            "agent. Use the provided incident information "
                            "and historical evidence carefully. "
                            "Do not invent historical incidents or evidence. "
                            "Clearly identify uncertainty and recommend "
                            "engineer verification before risky actions."
                        ),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                temperature=0.2,
            )

            return response.choices[0].message.content

        except Exception as error:
            last_error = error
            continue

    raise RuntimeError(
        f"LLM request failed with all configured models: {last_error}"
    )
