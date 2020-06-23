#web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
import urllib.request as request
import json
import pandas as pd

from web_app.services.strains_service import API  
from dotenv import load_dotenv

load_dotenv()


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
    ratings = DB.Column(DB.Integer, nullable = True)
    description = DB.Column(DB.String(500), nullable =True)

    def __repr__(self):
        return f"<Strains id ={self.id} name={self.name} race={self.race} medical={self.medical} positive={self.positive} negative={self.negative} flavors={self.flavors} ratings={self.ratings} description={self.description}>"

def extract_data(api=API):
    """
    Parses the json object readable dictionary 

    Param: api (connects to Strain API to get information about weed strains and effects)
    Returns: json data 
    Example:
    'Afpak': {'effects': {'medical': ['Depression',
                                   'Insomnia',
                                   'Pain',
                                   'Stress',
                                   'Lack of Appetite'],
                       'negative': ['Dizzy'],
                       'positive': ['Relaxed', 'Hungry', 'Happy', 'Sleepy']},
           'flavors': ['Earthy', 'Chemical', 'Pine'],
           'id': 1,
           'race': 'hybrid'},
    """

    with request.urlopen(API) as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')

    return data


def create_table(data, database=DB):
    """
    Uses json data and then inserts this information into a sqlite db
    Param: data(json object)
    Returns: items to be added to sql db
    Example:
    <id =1 name=Afpak race=hybrid medical=Depression,Insomnia,Pain,Stress,Lack of Appetite positive=Relaxed,Hungry,Happy,Sleepy negative=Dizzy flavors=Earthy,Chemical,Pine>
    """

    #Adding data from cannabis df to Strain record
    CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "csv", "cannabis.csv")
    cannabis = pd.read_csv(CSV_FILEPATH)
    
    small = cannabis[['rating', 'description']]

    cannabis_dict = small.set_index('rating')['description'].to_dict()

    #Creating a dictionary for the json object
    strains_dict = {'name': [],'race':[], 'medical':[], 'positive':[], 'negative':[], 'flavors':[], 'ratings':[], 'description':[]}


    for key, value in data.items():
        strain = Strain(name=key, race=value["race"], medical=','.join(value["effects"]["medical"]), positive=','.join(value["effects"]["positive"]), negative=','.join(value["effects"]["negative"]), flavors=','.join(value["flavors"]))

        DB.session.add(strain)

        strains_dict['name'].append(key)
        strains_dict['race'].append(value['race'])
        strains_dict['medical'].append(value['effects']['medical'])
        strains_dict['positive'].append(','.join(value['effects']['positive']))
        strains_dict['negative'].append(','.join(value['effects']['negative']))
        strains_dict['flavors'].append(','.join(value['flavors']))
        

    # for k,v in cannabis_dict.items():
    #     strain = Strain(ratings=k, description=v)

        # DB.session.add(strain)
   
    DB.session.commit()


def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON
    Param: database_records (a list of db.Model instances)
    Example: parse_records(User.query.all())
    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            <id =1 name=Afpak race=hybrid medical=Depression,Insomnia,Pain,Stress,Lack of Appetite positive=Relaxed,Hungry,Happy,Sleepy negative=Dizzy flavors=Earthy,Chemical,Pine>, 
        ]
    """
    parsed_records = []
    for record in database_records:
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records



