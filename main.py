from api.spotify_api import ServiceSpotify

service = ServiceSpotify()
token = service.get_token()

auth_header = service.get_auth_header()
print(auth_header)