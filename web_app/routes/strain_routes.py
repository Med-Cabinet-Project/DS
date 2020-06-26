#web_app/routes/strain_routes.py

from flask import Blueprint, request, render_template, flash, redirect, jsonify
from flask import Blueprint, request, render_template, flash, redirect, jsonify, make_response
import os
import pickle
import json

strain_routes = Blueprint("strain_routes", __name__)

#CORS requirement to access apis
@strain_routes.before_request
def before_request():
    """ CORS preflight, required for off-server access """

    def _build_cors_prelight_response():
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response

    if request.method == "OPTIONS":
        return _build_cors_prelight_response()

@strain_routes.after_request
def after_request(response):
    """ CORS headers, required for off-server access """

    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

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
@strain_routes.route('/types/<race>', methods=['GET'])
def get_type(race):

    """User can query Strains DB based on type/race preference - sativa, indica, hybrid"""

    records = Strain.query.filter_by(race=race).order_by(func.random()).limit(5).all()
    types = []
    for typ in records:
        types.append({
            "id":typ.id, 
            "name": typ.name,
            "type": typ.race,
            "medical":typ.medical, 
            "positive": typ.positive,
            "flavor": typ.flavors,
            "negative": typ.negative
        })
    return jsonify(types)

@strain_routes.route('/medical/<medical>', methods=['GET'])
def get_medical(medical):

    """User can query Strains DB based on medical symptoms/ailmens - depression, nausea, etc."""

    records = Strain.query.filter(Strain.medical.ilike(f"%{medical}%", escape="/")).order_by(func.random()).limit(5).all()
    
    medicals = []
    for med in records:
        medicals.append({
            "id":med.id, 
            "name": med.name,
            "type": med.race,
            "medical":med.medical, 
            "positive": med.positive,
            "flavor": med.flavors, 
            "negative": med.negative
        })
    return jsonify(medicals)

@strain_routes.route('/positive/<positive>', methods=['GET'])
def get_positve(positive):

    """User can query Strains DB based on positive effects they want to experience -euphoria, focus,  etc."""

    records = Strain.query.filter(Strain.positive.ilike(f"%{positive}%", escape="/")).order_by(func.random()).limit(5).all()
    
    positives = []
    for pos in records:
        positives.append({
            "id":pos.id, 
            "name": pos.name,
            "type": pos.race,
            "medical":pos.medical, 
            "positive": pos.positive,
            "flavor": pos.flavors, 
            "negative": pos.negative
        })
    return jsonify(positives)

@strain_routes.route('/flavors/<flavors>', methods=['GET'])
def get_flavors(flavors):

    """User can query Strains DB based on flavor preferences."""

    records = Strain.query.filter(Strain.flavors.ilike(f"%{flavors}%", escape="/")).order_by(func.random()).limit(5).all()
    
    tastes = []
    for tas in records:
        tastes.append({
            "id":tas.id, 
            "name": tas.name,
            "type": tas.race,
            "medical":tas.medical, 
            "positive": tas.positive,
            "flavor": tas.flavors, 
            "negative": tas.negative
        })
    return jsonify(tastes)