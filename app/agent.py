from app.memory import recall_memories, retain_memory
from app.llm import generate_response


def format_memories(memories):
    """Convert recalled Hindsight memories into readable context."""

    if not memories:
        return "No relevant historical incidents were found."

    formatted = []

    for index, memory in enumerate(memories, start=1):
        content = getattr(memory, "text", None)

        if not content:
            content = getattr(memory, "content", None)

        if not content:
            content = str(memory)

        formatted.append(
            f"Historical Incident {index}:\n{content}"
        )

    return "\n\n".join(formatted)


def triage_incident(alert, use_memory=True):
    """
    Analyze a new incident using historical memory when enabled.
    """

    memories = []

    if use_memory:
        try:
            response = recall_memories(alert)
            memories = response[:8] if response else []
        except Exception:
            memories = []

    historical_context = format_memories(memories)

    prompt = f"""
You are IncidentMind, an AI incident-response agent.

A new production alert has arrived.

NEW ALERT:
{alert}

HISTORICAL INCIDENT MEMORY:
{historical_context}

Analyze the incident using the historical evidence.

Provide:

1. Likely root cause
2. Similar historical incidents
3. Recommended next steps
4. Previously successful fixes
5. Fixes that failed previously, if known
6. Evidence supporting the recommendation
7. Risks or safety checks
8. Confidence level

Important rules:

- Do not invent historical incidents.
- Do not claim that a fix worked unless the memory provides evidence.
- Clearly distinguish historical evidence from your own reasoning.
- If there is weak or no historical evidence, say so.
- Recommendations must be reviewed and verified by an engineer.
"""

    answer = generate_response(prompt)

    return {
        "answer": answer,
        "memories": memories,
    }


def resolve_incident(
    incident_id,
    alert,
    root_cause,
    fix_applied,
    worked,
    minutes,
    lesson="",
):
    """
    Store the outcome of a resolved incident in Hindsight.
    """

    outcome = "WORKED" if worked else "FAILED"

    incident_summary = f"""
Incident ID: {incident_id}

Alert:
{alert}

Root Cause:
{root_cause}

Fix Applied:
{fix_applied}

Outcome:
{outcome}

Resolution Time:
{minutes} minutes

Lesson:
{lesson}
"""

    metadata = {
        "type": "incident_resolution",
        "incident_id": incident_id,
        "outcome": outcome,
    }

    return retain_memory(
        content=incident_summary,
        metadata=metadata,
    )
