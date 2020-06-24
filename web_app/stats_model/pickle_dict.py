import pandas as pd
import pickle
import os


cannabis = pd.read_csv(os.path.join(os.path.dirname(__file__), "cannabis.csv"))
cannabis_cleaned = cannabis.drop(['Unnamed: 0'], axis=1).copy()

print(cannabis_cleaned.columns)
print(cannabis_cleaned.isnull().sum())

columns = ['type', 'medical', 'positive', 'negative', 'flavor', 'rating','description']
cannabis_cleaned[columns] = cannabis_cleaned[columns].fillna("")

print(cannabis_cleaned.isnull().sum())

# breakpoint()
cannabis_dict = cannabis_cleaned.set_index('name')[['type', 'medical', 'positive', 'negative', 'flavor', 'rating','description']].T.to_dict('dict')

MODEL_FILEPATH = os.path.join(os.path.dirname(__file__), "strains.pkl")

with open(MODEL_FILEPATH, "wb") as model_file:
    print("SAVE MODEL")
    pickle.dump(cannabis_dict, model_file, protocol=pickle.HIGHEST_PROTOCOL)
    

