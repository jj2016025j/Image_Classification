# prompt/sd_api.py
import requests
from ai_image.config import MODEL_LIST_URL

def fetch_models():
    try:
        response = requests.get(MODEL_LIST_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching models: {e}")
        return []
      
if __name__ == '__main__':
    models = fetch_models()

    for model in models:
        print(f"model_name:{model['model_name']}")
