#web_app/stats_model/create_strain_csv.py

import requests
import json
from pprint import pprint
import pandas as pd
import numpy as np
from web_app.services.strains_service import API

#Downloading Info
r = requests.get(url=API)
data = r.json()
# pprint(data)

#Creating Table
#1 = First creating a dictionary
strains_dict = {'name': [],'race':[], 'medical':[], 'positive':[], 'negative':[], 'flavors':[]}

for key, value in data.items():
  strains_dict['name'].append(key)
  strains_dict['race'].append(value['race'])
  strains_dict['medical'].append(value['effects']['medical'])
  strains_dict['positive'].append(value['effects']['positive'])
  strains_dict['negative'].append(value['effects']['negative'])
  strains_dict['flavors'].append(value['flavors'])

#2. ext converting dictionary to dataframe
strains = pd.DataFrame.from_dict(strains_dict)

#Removing []
strains['medical'] = strains['medical'].str.join(',')
strains['positive'] = strains['positive'].str.join(',')
strains['negative'] = strains['negative'].str.join(',')
strains[ 'flavors'] = strains[ 'flavors'].str.join(',')

#Checking that it was changed properly
strains.head()

#4. Creating CSV
# strain.to_csv('strains.csv')
