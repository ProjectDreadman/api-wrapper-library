import requests
from .exceptions.py import APIWrapperError

class APIWrapper:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.example.com"

    def get(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            raise APIWrapperError(f"Error: {response.status_code}, {response.text}")

        return response.json()
