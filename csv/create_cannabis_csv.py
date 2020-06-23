#csv/create_cannabis_csv.py

import pandas as pd
import numpy as np
import os
from pprint import pprint

#Read CSV file
cannabis = pd.read_csv(os.path.join(os.path.dirname(__file__), "cannabis_sample.csv"))
strains = pd.read_csv(os.path.join(os.path.dirname(__file__), "strains.csv"))

#Checking that it displays properly
cannabis.head()
strains.head()

#Dropping unnecessary columns
strains = strains.drop(['Unnamed: 0'], axis=1)
cannabis = cannabis.drop(['Type', 'Effects', 'Flavor'], axis=1)

#Editing cannabis['Strain'] so that it can be compared to strains['name']
cannabis['Strain'] = cannabis['Strain'].str.replace('-', ' ')

#Changing ['Strain'] to name so that I can merge on this column
cannabis['name'] = cannabis['Strain']

#Choosing columns that I want to combine
cannabis = cannabis[['name', 'Rating', 'Description']]

#Merging two dataframes
cannabis = pd.merge(strains, cannabis, on="name", how="outer")

print(cannabis.head())

cannabis = pd.read_csv(os.path.join(os.path.dirname(__file__), "cannabis.csv"))


small = cannabis[['rating', 'description']]

cannabis_dict = small.set_index('rating')['description'].to_dict()
# pprint(cannabis_dict)

for key, value in cannabis_dict.items():
    print(key)
    print(value)
