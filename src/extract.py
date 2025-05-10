import requests
from src.auth import get_access_token



def get_track(track_id):
    token = get_access_token()
    headers = {"Authorization": f"Bearer  {token}"}
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    
    result = requests.get(url, headers=headers)
    if result.status_code == 200:
        return result.json()
    else:
        print(f"Error: {result.status_code}, {result.text}")
        return None