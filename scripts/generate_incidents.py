import json
from pathlib import Path


DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "incidents.json"
)


def check_incidents():
    """Check the existing incident dataset without changing it."""

    if not DATA_FILE.exists():
        print("incidents.json was not found.")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        incidents = json.load(file)

    print(f"Found {len(incidents)} incidents.")
    print(f"Dataset: {DATA_FILE}")

    if not incidents:
        print("Warning: dataset is empty.")
        return

    required_fields = [
        "id",
        "service",
        "severity",
        "symptoms",
        "root_cause",
        "fix_attempted",
        "fix_result",
        "resolution",
        "lessons_learned",
    ]

    first_incident = incidents[0]

    missing_fields = [
        field
        for field in required_fields
        if field not in first_incident
    ]

    if missing_fields:
        print("Missing fields:", missing_fields)
    else:
        print("Dataset structure looks correct.")

    print("\nSample incident:")
    print(json.dumps(first_incident, indent=4))


if __name__ == "__main__":
    check_incidents()
