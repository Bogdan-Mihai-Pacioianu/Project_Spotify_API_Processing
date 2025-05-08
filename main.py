from src import auth
from pprint import pprint
import json

token = auth.get_access_token()
print(token)