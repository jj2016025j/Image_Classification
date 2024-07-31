import requests

MODEL_LIST_URL = "http://127.0.0.1:7860/sdapi/v1/sd-models"

def fetch_models():
    response = requests.get(MODEL_LIST_URL)
    if response.status_code != 200:
        raise Exception("Failed to retrieve models")
    return response.json()
