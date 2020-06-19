
import os
import requests
import pprint
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://strainapi.evanbusse.com/"
ENDPOINT = "/strains/search/all"
URL = BASE_URL + API_KEY + ENDPOINT 

pp = pprint.PrettyPrinter(indent=4)

r = requests.get(url=URL)

data = r.json()

pp.pprint(data)