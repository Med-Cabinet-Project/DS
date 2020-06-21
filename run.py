# run.py
#Thinking aloud sheet 

#Attempts to extracts 
import os
import requests
import json
from pandas.io.json import json_normalize
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

#Accessing API
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://strainapi.evanbusse.com/"
ENDPOINT = "/strains/search/all"
URL = BASE_URL + API_KEY + ENDPOINT 

r = requests.get(url=URL)
data = r.json()

#Creating a dictionary for the json object
strands_dict = {'name': [], 'id': [], 'race':[], 'medical':[], 'positive':[], 'negative':[], 'flavors':[]}

for key, value in data.items():
    strands_dict['name'].append(key)
    strands_dict['race'].append(value['race'])
    strands_dict['medical'].append(value['effects']['medical'])
    strands_dict['positive'].append(value['effects']['positive'])
    strands_dict['negative'].append(value['effects']['negative'])
    strands_dict['flavors'].append(value['flavors'])

#Creating a table with the json object
strains_df = pd.DataFrame.from_dict(strands_dict)

print(strains_df.head())
print(strains_df.shape)

#Returning to html to load into sqlite db
strain_sql = strains_df.to_html(classes='strains'), titles=df.column.values)