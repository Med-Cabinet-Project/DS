
import pandas as pd
import numpy as np
import os

cannabis = pd.read_csv(os.path.join(os.path.dirname(__file__), "web_app", "stats_model", "cannabis.csv"))

symptom_1 = str(input("what is the first symptom: "))
sypmtom_2 = str(input("what is the second symptom: "))
positve_1 = str(input("what is a positve effect you'd like to experience: "))
positive_2 = str(input("what is a another positve effect you'd like to experience: "))

def sum_row(df): 
    for row in df:
        if symptom_1.isin(row['medical']):
            df['score'] += 0.5
        if  symptom_2.isin(row['medical']):
            df['score'] += 0.5
        if positive_1.isin(row['positive']):
            df['score'] += 0.5
        if positive_1.isin(row['positive']):
            df['score'] += 0.5
        else:
            0
    return df

cannabis.apply(sum_row)
