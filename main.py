import requests

class GeminiGPT:
    def __init__(self, api_key):
        self.api_url = "https://api.geminiai.com/gpt"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def query(self, prompt, max_tokens=100):
        data = {
            "prompt": prompt,
            "max_tokens": max_tokens
        }
        response = requests.post(self.api_url, headers=self.headers, json=data)
        return response.json()