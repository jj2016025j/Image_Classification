# prompt/sd_api.py
import requests
from ai_image.config import (
    SD_API_BASE_URL,
    MODEL_LIST_URL,
    CONFIG_URL,
    SAMPLER_LIST_URL,
    UPSCALER_LIST_URL,
    LORA_LIST_URL,
)

class SDClient:
    @staticmethod
    def fetch(endpoint):
        """Fetch data from the specified API endpoint."""
        try:
            response = requests.get(SD_API_BASE_URL + endpoint)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching data from {endpoint}: {e}")
            return []

    @staticmethod
    def get_models():
        """Fetch the list of available models."""
        return SDClient.fetch(MODEL_LIST_URL)

    @staticmethod
    def get_config():
        """Fetch the configuration details."""
        return SDClient.fetch(CONFIG_URL)

    @staticmethod
    def get_samplers():
        """Fetch the list of available samplers."""
        return SDClient.fetch(SAMPLER_LIST_URL)

    @staticmethod
    def get_upscalers():
        """Fetch the list of available upscalers."""
        return SDClient.fetch(UPSCALER_LIST_URL)

    @staticmethod
    def get_loras():
        """Fetch the list of available LoRAs."""
        return SDClient.fetch(LORA_LIST_URL)