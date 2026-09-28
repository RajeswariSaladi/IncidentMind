import json
from pathlib import Path

from hindsight_client import Hindsight

from app.config import (
    HINDSIGHT_API_KEY,
    HINDSIGHT_BASE_URL,
    BANK_ID,
)


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "incidents.json"


def get_client():
    return Hindsight(
        api_key=HINDSIGHT_API_KEY,
        base_url=HINDSIGHT_BASE_URL,
    )


def seed_incidents():
    client = get_client()

    # Create the memory bank if it does not already exist
    try:
        client.create_bank(
            bank_id=BANK_ID,
            name="IncidentMind Team Memory",
            mission=(
                "Remember production incidents, root causes, "
                "successful fixes, failed fixes, and operational lessons."
            ),
        )
        print(f"Created memory bank: {BANK_ID}")
    except Exception:
        print(f"Using existing memory bank: {BANK_ID}")

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        incidents = json.load(file)

    for incident in incidents:
        content = f"""
Incident ID: {incident.get("id")}
Service: {incident.get("service")}
Severity: {incident.get("severity")}
Timestamp: {incident.get("timestamp")}

Alert:
{incident.get("alert")}

Root Cause:
{incident.get("root_cause")}

Fix Applied:
{incident.get("fix")}

Outcome:
{incident.get("outcome")}

Lesson:
{incident.get("lesson")}
"""

        metadata = {
            "type": "historical_incident",
            "incident_id": incident.get("id"),
            "service": incident.get("service"),
            "severity": incident.get("severity"),
            "outcome": incident.get("outcome"),
        }

        client.retain(
            bank_id=BANK_ID,
            content=content,
            metadata=metadata,
        )

        print(f"Stored: {incident.get('id')}")

    print(f"\nSuccessfully seeded {len(incidents)} incidents.")


if __name__ == "__main__":
    seed_incidents()
