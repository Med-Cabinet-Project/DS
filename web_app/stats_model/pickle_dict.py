import pandas as pd
import pickle
import os
from pprint import pprint


#Pickle dictionary for string routes
cannabis = pd.read_csv(os.path.join(os.path.dirname(__file__), "cannabis.csv"))
cannabis['description'] = cannabis['description'].str.strip()
cannabis_cleaned = cannabis.drop(['Unnamed: 0'], axis=1).copy()

columns = ['type', 'medical', 'positive', 'negative', 'flavor', 'rating','description']
cannabis_cleaned[columns] = cannabis_cleaned[columns].fillna("")

cannabis_dict = cannabis_cleaned.set_index('name')[['type', 'medical', 'positive', 'negative', 'flavor', 'rating','description']].T.to_dict('dict')

MODEL_FILEPATH = os.path.join(os.path.dirname(__file__), "strains.pkl")

with open(MODEL_FILEPATH, "wb") as model_file:
    print("SAVE PICKLE 1")
    pickle.dump(cannabis_dict, model_file, protocol=pickle.HIGHEST_PROTOCOL)


#Pickle dictionary for numbered routes
cannabis_num_dict = {}
cannabis_num_dict = {i:(k,v) for (i), (k,v) in zip(cannabis['Unnamed: 0'], cannabis_dict.items())}
# pprint(cannanbis_num_dict)

MODEL2_FILEPATH = os.path.join(os.path.dirname(__file__), "strains_num.pkl")

with open(MODEL2_FILEPATH, "wb") as model_file:
    print("SAVE PICKLE 2")
    pickle.dump(cannabis_num_dict, model_file, protocol=pickle.HIGHEST_PROTOCOL)
