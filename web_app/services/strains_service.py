#web_app/services/strain_services.py

import os
import urllib.request as request
import json

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://strainapi.evanbusse.com/"
ENDPOINT = "/strains/search/all"
API = BASE_URL + API_KEY + ENDPOINT 

if __name__ == "__main__":
   pass
    