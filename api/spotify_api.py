from dotenv import load_dotenv
from requests import post, get, delete
import os
import base64
import json

class ServiceSpotify:
    
    load_dotenv()

    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secrets = os.getenv('SPOTIFY_CLIENT_SECRETS')
    redirected_url = os.getenv('SPOTIFY_TOKEN_URL')
    get_playlist_url = os.getenv('GET_PLAYLIST_URL')
    get_artist_url = os.getenv('GET_ARTIST_URL')

    def get_token(self):
        auth_string = self.client_id + ':' + self.client_secrets
        auth_bytes = auth_string.encode('utf-8')
        auth_base64 = str(base64.b64encode(auth_bytes),'utf-8')

        url = self.redirected_url
        headers = {
            'Authorization': 'Basic ' + auth_base64,
            'Content_Type' : 'application/x-www-form-urlencoded'
        }
        data = {'grant_type': 'client_credentials'}

        result = post(url, headers=headers, data=data)
        json_response = json.loads(result.content)
        token = json_response['access_token']
        return token

    def get_auth_header(self, token):
        return {'Authorization': f'Bearer {token}'}

    def get_artist(self, token, artist_id):
        try:
            if not token or not artist_id:
                raise ValueError("Token and artist_id are required")
            
            url = self.get_artist_url + artist_id
            headers = self.get_auth_header(token)
            results = get(url, headers=headers)
            json_response = json.loads(results.content)
            return json_response
        
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return None
        
    def get_playlists(self, token, playlist_id):
        url = self.get_playlist_url + playlist_id
        headers = self.get_auth_header(token)
        result = get(url, headers=headers)
        json_response = json.loads(result.content)
        return json_response