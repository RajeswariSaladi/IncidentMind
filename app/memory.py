from hindsight_client import Hindsight

from app.config import (
    HINDSIGHT_API_KEY,
    HINDSIGHT_BASE_URL,
    BANK_ID,
)


def get_client():
    """Create and return a Hindsight client."""
    return Hindsight(
        base_url=HINDSIGHT_BASE_URL,
        api_key=HINDSIGHT_API_KEY,
    )


def retain_memory(content, metadata=None):
    """Store an incident or resolution in Hindsight memory."""
    client = get_client()

    return client.retain(
        bank_id=BANK_ID,
        content=content,
        metadata=metadata or {},
    )


def recall_memories(query):
    """Retrieve memories related to a new incident."""
    client = get_client()

    response = client.recall(
        bank_id=BANK_ID,
        query=query,
    )

    return response.results


def reflect_on_incidents(question):
    """Generate higher-level insights from stored incident memories."""
    client = get_client()

    response = client.reflect(
        bank_id=BANK_ID,
        query=question,
    )

    return response


def close_client():
    """Reserved for future client lifecycle management."""
    return None
