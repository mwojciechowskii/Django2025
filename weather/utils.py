from typing import Any
import requests

def requestJSON(url: str) -> Any:

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()
