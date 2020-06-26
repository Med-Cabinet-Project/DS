
import pandas as pd
import numpy as np
import os

cannabis = pd.read_csv(os.path.join(os.path.dirname(__file__), "web_app", "stats_model", "cannabis.csv"))

cannabis['medical'] = cannabis['medical'].astype(str)
cannabis['positive'] = cannabis['positive'].astype(str)


symptom_1 = str(input("what is the first symptom: "))
sypmtom_2 = str(input("what is the second symptom: "))
positve_1 = str(input("what is a positve effect you'd like to experience: "))
positive_2 = str(input("what is a another positve effect you'd like to experience: "))

def sum_row(df): 
    for row in df:
        if row['medical'].str.contains('symptom_1'):
            df['score'] += 0.5
        if row['medical'].str.contains('symptom_1'):
            df['score'] += 0.5
        if row['positive'].str.contains('positive'):
            df['score'] += 0.5
        if row['positive'].str.contains('positive'):
            df['score'] += 0.5
        else:
            0
    return df['score']

cannabis.apply(sum_row)
