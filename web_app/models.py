#web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB = SQLAlchemy()

migrate = Migrate()

class Strain(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    medical = db.Column(db.String(128), nullable = False)
    positive = db.Column(db.String(128), nullable = False)
    negative = db.Column(db.String(128), nullable = True)
    flavor = db.Column(db.String(128), nullable = False)
    race = db.Column(db.String(128), nullable = False)

    def __repr__(self):
        return f"<Strain {self.id} {self.name}{self.medical}{self.positive} {self.negative}{self.flavor} >"


#Need to create helper function 
# working with parse_records for an example
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

#Also look at helper functions in OpenAQ
def get_records(city="Los Angeles", parameter="pm25"):
    status, body = api.measurements(city=city, parameter=parameter)

    records = []

    observations = [(res['date']['utc'], res['value'])
                    for res in body['results']]
    for obs in observations:
        records.append(Record(datetime=obs[0], value=obs[1]))
                    
    return records


def add_records(records, database=DB):
  for r in records: 
    # print(r) checking if records are being created
    DB.session.add(r)
  DB.session.commit()