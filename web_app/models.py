#web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Strain(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    medical_needs = db.Column(db.String(128), nullable = False)
    effects_positive = db.Column(db.String(128), nullable = False)
    effects_negative = db.Column(db.String(128), nullable = True)
    flavor = db.Column(db.String(128), nullable = False)
    race = db.Column(db.String(128), nullable = False)

    def __repr__(self):
        return f"<Strain {self.id} {self.name}{self.medical_needs}{self.effects_positive} {self.effects_negative}{self.flavor} >"


