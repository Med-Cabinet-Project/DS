
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

# print("---DATA ITEMS----")
for (k, v) in data.items():
    print("Key: " + k)
    print("Value: " + str(v))

print("---STRAND----")

strands_dict = {'name': [], 'id': [], 'race':[], 'medical':[], 'positive':[], 'negative':[], 'flavors':[]}
for key, value in data.items():
    strands_dict['name'].append(key)
    strands_dict['id'].append(value['id'])
    strands_dict['race'].append(value['race'])
    strands_dict['medical'].append(value['effects']['medical'])
    strands_dict['positive'].append(value['effects']['positive'])
    strands_dict['negative'].append(value['effects']['negative'])
    strands_dict['flavors'].append(value['flavors'])



pprint(strands_dict)

#Creating a pandas dataframe with the dictionary

