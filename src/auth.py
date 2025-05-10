from dotenv import load_dotenv
import json
import requests
import base64
import os

load_dotenv()


def get_access_token():
    client_id = os.getenv("SPOTYFY_CLIENT_ID")
    client_secret = os.getenv("SPOTYFY_CLIENT_SECRET")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None