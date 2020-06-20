import requests
import os
from pprint import pprint 
from dotenv import load_dotenv

load_dotenv()

# Grab keys and tokens from .env
API_1_KEY = os.getenv('API_1_KEY', default='Oops')

# URLs
EFFECTS_ENDPOINT = '/searchdata/effects'
BASE_1_URL = 'http://strainapi.evanbusse.com/'


URL = BASE_1_URL + API_1_KEY + EFFECTS_ENDPOINT
r = requests.get(url=URL)
data = r.json()
pprint(data)
