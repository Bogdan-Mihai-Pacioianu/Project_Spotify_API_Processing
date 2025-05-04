from api.spotify_api import ServiceSpotify
from pprint import pprint
import json

service = ServiceSpotify()
token = service.get_token()
aut_header = service.get_auth_header(token=token)

# https://open.spotify.com/playlist/37i9dQZF1DZ06evO1ZTFXr?si=e0b996bcd0434249

playlists = service.get_playlists(token=token, playlist_id='3cEYpjA9oz9GiPac4AsH4n')
pprint(playlists)

print ("======================================")
artist = service.get_artist(token=token, artist_id="1q1wfzh2xtpj27TnIAqIvd")
print(json.dumps(artist, indent=2))   

artist_list = []

