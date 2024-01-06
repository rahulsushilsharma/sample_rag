import requests
import json

class CustomEmbeddingFunction:
    def __init__(self, api_path, api_key):
        self.api_key = api_key
        self.api_path = api_path

    def generate(self, texts):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "inputs": texts
        }

        try:
            response = requests.post(self.api_path, headers=headers, data=json.dumps(data))
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
            raise ValueError('Failed to fetch')

        try:
            result = response.json()
        except json.JSONDecodeError as e:
            print(e)
            raise ValueError('Unknown response')

        return result

# Example usage:
# Replace 'your_api_path' and 'your_api_key' with actual values
