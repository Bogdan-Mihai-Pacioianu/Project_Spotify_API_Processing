import spotipy
from dotenv import load_dotenv
from requests import post, get, delete
import os
import base64
import json

class ServiceSpotify:
    load_dotenv()

    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secrets = os.getenv('SPOTIFY_CLIENT_SECRETS')
    redirected_url = os.getenv('SPOTIFY_REDIRECTED_URL')

    def get_token(self):
        auth_string = self.client_id + ':' + self.client_secrets
        auth_bytes = auth_string.encode('utf-8')
        auth_base64 = str(base64.b64encode(auth_bytes),'utf-8')

        url = self.redirected_url + '/token'
        headers = {
            'Authorization': 'Basic ' + auth_base64,
            'Content_Type' : 'application/x-www-form-urlencoded'
        }
        data = {'grant_type': 'client_credentials'}

        result = post(url, headers=headers, data=data)
        json_response = json.loads(result.content)
        token = json_response['access_token']
        return token

    def get_auth_header(token):
        return {'Authorization': 'Bearer ' + token}

