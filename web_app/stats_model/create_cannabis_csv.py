#csv/create_cannabis_csv.py

import pandas as pd
import numpy as np
import os
from pprint import pprint

#Read CSV file
cannabis_sample = pd.read_csv(os.path.join(os.path.dirname(__file__), "csv", "cannabis_sample.csv"))
strains = pd.read_csv(os.path.join(os.path.dirname(__file__), "csv", "strains.csv"))

#Checking that it displays properly
cannabis.head()
strains.head()

#Dropping unnecessary columns
strains = strains.drop(['Unnamed: 0'], axis=1)

#Editing cannabis['name'] so that it can be compared to strains['name']
strains['name'] = strains['name'].str.replace(' ', '-')

#Changing ['Strain'] to name so that I can merge on this column
cannabis_sample['name'] = cannabis['Strain']
cannabis_sample['positive'] = cannabis_sample['Effects']
cannabis_sample['flavors'] = cannabis_sample['Flavor']
cannabis_sample = cannabis_sample.drop(['Strain', 'Effects', 'Flavor'], axis=1)

#Changing ['race'] to type so that I can merge on this column
strains['Type'] = strains['race']
strains = strains.drop(['race'], axis=1)

#Merging two dataframes
cannabis = pd.merge(strains, cannabis, on="name", how="outer")

#Checking out new dataframe
cannabis.isnull().sum()

print(cannabis.head())

#Converting null values to NaN
columns = ['positive_x', 'flavors_x', 'Type_x']
cannabis[columns] = cannabis[columns].fillna(np.NaN)
cannabis['Type_x'] = cannabis.loc[cannabis['Type_x'] == np.NaN,'Type_x'] = cannabis['Type_y']
cannabis['flavors_x'] = cannabis.loc[cannabis['flavors_x'] == np.NaN,'flavors_x'] = cannabis['flavors_y']
cannabis['positive_x'] = cannabis.loc[cannabis['positive_x'] == np.NaN,'positive_x'] = cannabis['positive_y']

#Checking out columns after filling na
cannabis.isnull().sum()

#Dropping redundant columns
cannabis = cannabis.drop(['positive_y', 'flavors_y', 'Type_y'], axis=1)

cannabis.shape

#Clean up
cannabis['name']=cannabis['name'].str.replace('- ', '-')
cannabis['name']=cannabis['name'].astype(str)
cannabis['name']=cannabis['name'].str.replace('""', '')