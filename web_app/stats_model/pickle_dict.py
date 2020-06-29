#web_app/stats_model/pickle_dict.py

import pandas as pd
import pickle
import os
from pprint import pprint

#Clean cannabis csv
cannabis = pd.read_csv(os.path.join(os.path.dirname(__file__), "csv", "cannabis.csv"))
cannabis['description'] = cannabis['description'].str.strip()
cannabis_cleaned = cannabis.copy()

columns = ['type', 'medical', 'positive', 'negative', 'flavor', 'rating','description']
cannabis_cleaned[columns] = cannabis_cleaned[columns].fillna("")

#Pickle dictionary for strains route
cannabis_dict = cannabis_cleaned.set_index('name')[['type', 'medical', 'positive', 'negative', 'flavor', 'rating','description']].T.to_dict('dict')

MODEL_FILEPATH = os.path.join(os.path.dirname(__file__), "pickle_models", "strains.pkl")

with open(MODEL_FILEPATH, "wb") as model_file:
    print("SAVE PICKLE 1")
    pickle.dump(cannabis_dict, model_file, protocol=pickle.HIGHEST_PROTOCOL)


#Pickle dictionary for numbered routes
cannabis_ordered = cannabis_cleaned.to_dict(orient='records')

MODEL2_FILEPATH = os.path.join(os.path.dirname(__file__), "pickle_models", "strains_num.pkl")

with open(MODEL2_FILEPATH, "wb") as model_file:
    print("SAVE PICKLE 2")
    pickle.dump(cannabis_ordered, model_file, protocol=pickle.HIGHEST_PROTOCOL)




