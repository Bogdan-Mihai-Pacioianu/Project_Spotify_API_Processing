from dotenv import load_dotenv
import json
import requests
import base64
import os

load_dotenv()

def get_access_token():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRETS")
    url = os.getenv("SPOTIFY_TOKEN_URL")
    headers = {
    "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]