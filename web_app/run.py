
import os
import requests
import urllib.request as request
import json
from pprint import pprint 
from dotenv import load_dotenv
import numpy as np 

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://strainapi.evanbusse.com/"
ENDPOINT = "/strains/search/all"
URL = BASE_URL + API_KEY + ENDPOINT 

#Get all the strains and information about effects
r = requests.get(url=URL)
data = r.json()
# pprint(data)

#Exploring data and seeing how to extract specific values
with request.urlopen(URL) as response:
    if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


# pprint(type(data))
print(len(data.keys())) # 1970 different strains will not be possible to call each one separately
# pprint(data.keys())   

print("---DATA ITEMS----")
print(data.items())


print("---STRAND----")

strands_dict = {'name': [], 'medical':[], 'positive_effects':[], ''}
for key in data.keys():
    strands.append(key)

print(strands)



print("---RES----")
effects = data['effects']
print(effects)
