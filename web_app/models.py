#web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
import os
import urllib.request as request
import json
from web_app.services.strains_service import API  
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL") 

DB = SQLAlchemy()

migrate = Migrate()

class Strain(DB.Model):
    __tablename__ = "strains"
    id = DB.Column(DB.Integer, primary_key = True, autoincrement=True)
    name = DB.Column(DB.String(128), nullable = True)
    race = DB.Column(DB.String(128), nullable = True)
    medical = DB.Column(DB.String(500), nullable = True)
    positive = DB.Column(DB.String(500), nullable = True)
    negative = DB.Column(DB.String(500), nullable = True)
    flavors = DB.Column(DB.String(128), nullable = True)

    def __repr__(self):
        return f"<id ={self.id} name={self.name} race={self.race} medical={self.medical} positive={self.positive} negative={self.negative} flavors={self.flavors}>"

def create_table(api=API):
    with request.urlopen(API) as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')

    #Creating a dictionary for the json object
    strains_dict = {'name': [],'race':[], 'medical':[], 'positive':[], 'negative':[], 'flavors':[]}

    for key, value in data.items():
        strains_dict['name'].append(key)
        strains_dict['race'].append(value['race'])
        strains_dict['medical'].append(value['effects']['medical'])
        strains_dict['positive'].append(value['effects']['positive'])
        strains_dict['negative'].append(value['effects']['negative'])
        strains_dict['flavors'].append(value['flavors'])

    #Creating a table from the strains dictionary
    strains_df = pd.DataFrame.from_dict(strains_dict, orient='index')
    strains_df = strains_df.transpose()

    #removing [] from the last four columns 
    # strains_df[['medical', 'positive', 'negative', 'flavors']] = strains_df[['medical', 'positive', 'negative', 'flavors']].str.join(',')
    strains_df['medical'] = strains_df['medical'].str.join(',')
    strains_df['positive'] = strains_df['positive'].str.join(',')
    strains_df['negative'] = strains_df['negative'].str.join(',')
    strains_df[ 'flavors'] = strains_df[ 'flavors'].str.join(',')

    Strain.name = strains_df.name
    Strain.race = strains_df.race
    Strain.medical = strains_df.medical
    Strain.positive = strains_df.positive
    Strain.negative = strains_df.negative
    Strain.flavors = strains_df.flavors

    return strains_df

def add_table(strains_df, database=DB):

    engine = create_engine(DATABASE_URL)
    strains = strains_df.to_sql('strains', engine, if_exists='replace')

    DB.session.commit()

    return strains

def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON
    Param: database_records (a list of db.Model instances)
    Example: parse_records(User.query.all())
    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records


# def get_records(city="Los Angeles", parameter="pm25"):
#     status, body = api.measurements(city=city, parameter=parameter)

#     records = []

#     observations = [(res['date']['utc'], res['value'])
#                     for res in body['results']]
#     for obs in observations:
#         records.append(Record(datetime=obs[0], value=obs[1]))
                    
#     return records


# def add_records(records, database=DB):
#   for r in records: 
#     # print(r) checking if records are being created
#     DB.session.add(r)
#   DB.session.commit()

