from src.extract import get_track
from pprint import pprint
import json

#https://open.spotify.com/track/5On1Z1lSOxRzTQ2N0aOTd6?si=c1dccc42c5e64a94

track = get_track("5On1Z1lSOxRzTQ2N0aOTd6")
pprint(track)