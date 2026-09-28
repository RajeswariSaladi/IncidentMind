import os
from hindsight_client import Hindsight

def get_client():
    return Hindsight(
        api_key=os.getenv("HINDSIGHT_API_KEY"),
        base_url=os.getenv(
            "HINDSIGHT_BASE_URL",
            "https://api.hindsight.vectorize.io"
        )
    )
