
import pandas as pd
import numpy as np
import re
import os

cannabis = pd.read_csv(os.path.join(os.path.dirname(__file__), "web_app", "stats_model", "cannabis.csv"))

cannabis['medical'] = cannabis['medical'].astype(str)
cannabis['positive'] = cannabis['positive'].astype(str)


symptom_1 = input("what is the first symptom: ")#"pain|"
cannabis['score1'] = np.where(cannabis['medical'].str.contains((symptom_1), flags=re.IGNORECASE, regex=True), +0.5, 0)

symptom_2 = input("what is the second symptom: ")#"headache|" 
cannabis['score2'] = np.where(cannabis['medical'].str.contains((symptom_2), flags=re.IGNORECASE, regex=True), +0.5, 0)

positive_1 = input("what is a positve effect you'd like to experience: ")#"euphoria" 
cannabis['score3'] = np.where(cannabis['positive'].str.contains((positive_1), flags=re.IGNORECASE, regex=True), +0.5, 0)

positive_2 = input("what is a another positve effect you'd like to experience: ")#"relaxed" 
cannabis['score4'] = np.where(cannabis['positive'].str.contains((positive_2), flags=re.IGNORECASE, regex=True), +0.5, 0)

cannabis['score'] = cannabis['score1']+cannabis['score2']+cannabis['score3']+cannabis['score4']

print(cannabis['score'].to_string())

