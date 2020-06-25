#web_app/routes/strain_routes.py

from flask import Blueprint, request, render_template, flash, redirect, jsonify
import os
import pickle
import json
import random
from sqlalchemy.sql.expression import func
from web_app.models import DB, Strain, extract_data, create_table, parse_records
from web_app.services.strains_service import API 
from pprint import pprint

strain_routes = Blueprint("strain_routes", __name__)

@strain_routes.route("/", methods=['GET', 'POST'])
def root():
    """
        Return first 100 strains in pickle dict
    """
    PICKLE2_FILEPATH = os.path.join(os.path.dirname(__file__),"..", "stats_model", "strains_num.pkl")
    pickle2_dict = pickle.load(open(PICKLE2_FILEPATH, "rb"))

    return jsonify(pickle2_dict)

@strain_routes.route("/<strain>", methods=['GET'])
def get_strain(strain):
    """
        Can query pickled strains dictionary to get information about a particular strain
    """
    PICKLE_FILEPATH = os.path.join(os.path.dirname(__file__),"..", "stats_model", "strains.pkl")
    pickle_dict = pickle.load(open(PICKLE_FILEPATH, "rb"))

    return jsonify({"strain":pickle_dict[strain]})


@strain_routes.route('/data', methods=["GET", "POST"])
def data():
    """View all strains in database."""

    DB.drop_all()
    DB.create_all()

    create_table(extract_data())
    strain = Strain.query.all()
    records = parse_records(strain)
    
    return render_template("data.html", records=records, message="Home Page")


#More query routes 
#https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html
@strain_routes.route('/types/<race>', methods=['GET'])
def get_type(race):

    records = Strain.query.filter_by(race = race).order_by(func.random()).limit(5).all()
    types = []
    for typ in records:
        types.append({
            "id":typ.id, 
            "name": typ.name,
            "medical":typ.medical, 
            "positive": typ.positive,
            "flavor": typ.flavors
        })
    return jsonify(types)

@strain_routes.route('/medical/<medical>', methods=['GET'])
def get_medical(medical):
    records = Strain.query.filter(Strain.medical.ilike(f"%{medical}%", escape="/")).order_by(func.random()).limit(5).all()
    
    medicals = []
    for med in records:
        medicals.append({
            "id":med.id, 
            "name": med.name,
            "medical":med.medical, 
            "positive": med.positive,
            "flavor": med.flavors
        })
    return jsonify(medicals)

@strain_routes.route('/positive/<positive>', methods=['GET'])
def get_positve(positive):
    records = Strain.query.filter(Strain.positive.ilike(f"%{positive}%", escape="/")).order_by(func.random()).limit(5).all()
    
    positives = []
    for pos in records:
        positives.append({
            "id":pos.id, 
            "name": pos.name,
            "medical":pos.medical, 
            "positive": pos.positive,
            "flavor": pos.flavors
        })
    return jsonify(positives)

@strain_routes.route('/flavors/<flavors>', methods=['GET'])
def get_flavors(flavors):
    records = Strain.query.filter(Strain.flavors.ilike(f"%{flavors}%", escape="/")).order_by(func.random()).limit(5).all()
    
    tastes = []
    for tas in records:
        tastes.append({
            "id":tas.id, 
            "name": tas.name,
            "medical":tas.medical, 
            "positive": tas.positive,
            "flavor": tas.flavors
        })
    return jsonify(tastes)