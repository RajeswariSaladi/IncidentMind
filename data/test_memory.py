import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    api_key=os.getenv("HINDSIGHT_API_KEY"),
    base_url=os.getenv(
        "HINDSIGHT_BASE_URL",
        "https://api.hindsight.vectorize.io"
    )
)

results = client.recall(
    "Payment API database connection pool exhausted",
    limit=5
)

print("Recalled incidents:")
for result in results:
    print(result)
