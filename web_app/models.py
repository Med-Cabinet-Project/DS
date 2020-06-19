#web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Strain(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    strain = db.Column(db.String(128))

    def __repr__(self):
        return f"<Strain {self.id} {self.strain}>"


class Medical(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    medical_needs = db.Column(db.String(128), nullable = False)

    def __repr__(self):
        return f"<Medical {self.id} {self.medical_needs}>"

class Effects(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    effects_positive = db.Column(db.String(128), nullable = False)
    effects_negative = db.Column(db.String(128), nullable = True)

    def __repr__(self):
        return f"<Positive Effects {self.id} {self.effects_positive} {self.effects_negative}>"

class Flavors(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    tastes_like = db.Column(db.String(128), nullable = False)

    def __repr__(self):
        return f"<Tastes Like {self.id} {self.tastes_like}>"

class Race(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    race = db.Column(db.String(128), nullable = False)

    def __repr__(self):
        return f"<Race {self.id} {self.race}>"