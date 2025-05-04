from api.spotify_api import ServiceSpotify

service = ServiceSpotify()
token = service.get_token()
print(token)
aut_header = service.get_auth_header(token=token)
print(aut_header)