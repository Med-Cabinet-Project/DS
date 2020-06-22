#web_app/services/strain_services.py

import os
import urllib.request as request
import json
from pprint import pprint 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://strainapi.evanbusse.com/"
ENDPOINT = "/strains/search/all"
API = BASE_URL + API_KEY + ENDPOINT 

if __name__ == "__main__":
    #Exploring data and seeing how to extract specific values
    with request.urlopen(API) as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')

    pprint(type(data))
    print(len(data.keys())) # 1970 different strains will not be possible to call each one separately

    print("---STRAND----")

    strands_dict = {'name': [], 'id': [], 'race':[], 'medical':[], 'positive':[], 'negative':[], 'flavors':[]}

    for key, value in data.items():
        strands_dict['id'].append(value['id'])
        strands_dict['name'].append(key)
        strands_dict['race'].append(value['race'])
        strands_dict['medical'].append(value['effects']['medical'])
        strands_dict['positive'].append(value['effects']['positive'])
        strands_dict['negative'].append(value['effects']['negative'])
        strands_dict['flavors'].append(value['flavors'])

    print(strands_dict)


    name_dict = {'name': []}
    id_dict =  {'id': []},
    race_dict = {'race':[]}
    medical_dict = {'medical':[]}
    positive_dict =  {'positive':[] }
    negative_dict = {'negative':[] }
    flavors_dict = {'flavors':[]}
    
    for key, value in data.items():
        name_dict['name'].append(key)
        id_dict['id'].append(value['id'])
        race_dict['race'].append(value['race'])
        medical_dict['medical'].append(value['effects']['medical'])
        positive_dict['positive'].append(value['effects']['positive'])
        negative_dict['negative'].append(value['effects']['negative'])
        flavors_dict['flavors'].append(value['flavors'])

    pprint(name_dict)
    pprint(id_dict)
    pprint(race_dict)
    pprint(medical_dict)



    