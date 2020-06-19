import requests, os
from dotenv import load_dotenv
import pprint

load_dotenv()

# Grab keys and tokens from .env
API_1_KEY = os.getenv('API_1_KEY', default='Oops')
BASE_1_URL = os.getenv('BASE_1_URL', default='Oops')

# URLs
EFFECTS_ENDPOINT = '/searchdata/effects'

pp = pprint.PrettyPrinter(indent=4)

URL = BASE_1_URL + API_1_KEY + EFFECTS_ENDPOINT
r = requests.get(url=URL)
data = r.json()
pp.pprint(data)
