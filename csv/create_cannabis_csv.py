import pandas as pd
import numpy as np

#Read CSV file
cannabis = pd.read_csv('https://raw.githubusercontent.com/Med-Cabinet-Project/DS/master/CSV/cannabis_sample.csv')
strains = pd.read_csv('https://raw.githubusercontent.com/Med-Cabinet-Project/DS/master/CSV/strains.csv')

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

cannabis.head()