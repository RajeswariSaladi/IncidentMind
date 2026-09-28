import os
from dotenv import load_dotenv
from hindsight_client import Hindsight
from incident_data import load_incidents

load_dotenv()

client = Hindsight(
    api_key=os.getenv("HINDSIGHT_API_KEY"),
    base_url=os.getenv(
        "HINDSIGHT_BASE_URL",
        "https://api.hindsight.vectorize.io"
    )
)

incidents = load_incidents()

for incident in incidents:
    client.retain(
        content=str(incident),
        metadata={
            "type": "historical_incident",
            "incident_id": incident["id"],
            "service": incident["service"],
            "severity": incident["severity"]
        }
    )

print(f"Loaded {len(incidents)} incidents into Hindsight memory.")
