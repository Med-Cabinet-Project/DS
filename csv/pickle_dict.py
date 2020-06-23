import pandas as pd
import numpy as np
import os
from pprint import pprint

cannabis = pd.read_csv(os.path.join(os.path.dirname(__file__), "cannabis.csv"))
cannabis = cannabis.drop(["Unnamed: 0"], axis=1)

print(cannabis.columns)

cannabis_dict = cannabis.set_index('name')[['race', 'medical', 'positive', 'negative', 'flavors', 'rating','description']].T.to_dict('dict')

print(len(cannabis_dict))
pprint(cannabis_dict)