#web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
import urllib.request as request
import json
from web_app.services.strains_service import API  

DB = SQLAlchemy()

migrate = Migrate()

class Strain(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    name = DB.Column(DB.String(128))
    race = DB.Column(DB.String(128), nullable = False)
    medical = DB.Column(DB.String(500), nullable = True)
    positive = DB.Column(DB.String(500), nullable = False)
    negative = DB.Column(DB.String(500), nullable = True)
    flavors = DB.Column(DB.String(128), nullable = False)

    def __repr__(self):
        return f"<Strain {self.id} {self.name} {self.race} {self.medical} {self.positive} {self.negative} {self.flavors} >"

def get_records(api=API):
    with request.urlopen(API) as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')

    records = []

    observations = [(k, v['race'], v['effects']['medical'], v['effects']['positive'], v['effects']['negative'], v['flavors'])
                    for k,v in data.items()]
    for obs in observations:
        records.append(Strain(name=obs[0], race=obs[1], medical=obs[2], positive=obs[3], negative=obs[4], flavors=obs[5]))
                    
    return records


def add_records(records, database=DB):
    
  for r in records: 
    DB.session.add(r)

  DB.session.commit()