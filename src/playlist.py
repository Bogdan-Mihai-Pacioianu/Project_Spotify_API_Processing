from auth import get_access_token
from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()

def get_playlists(user_id, get_access_token):
    url = os.getenv("SPOTIFY_PLAYLISTS_URL").format(user_id=user_id)
    headers = {