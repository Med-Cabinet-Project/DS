#web_app/routes/strain_routes.py

from flask import Blueprint, render_template, flash, redirect, jsonify
import requests
import pickle
import os
from web_app.models import DB, Strain, extract_data, create_table, parse_records
from web_app.services.strains_service import API 
from pprint import pprint



strain_routes = Blueprint("strain_routes", __name__)

PICKLE_FILEPATH = os.path.join(os.path.dirname(__file__),"..", "stats_model", "strains.pkl")
pickle_dict = pickle.load(open(PICKLE_FILEPATH, "rb"))

@strain_routes.route("/", methods=['GET', 'POST'])
def root():
    """
        Return first 100 strains in pickle dict
    """
    new_d = {}
    counter = 0
    n = 10 # number of first items
    
    for k,v in pickle_dict.items(): 
        new_d[k] = v 

        if counter >= n: 
            counter+=1
            print(new_d)

    return jsonify(new_d)

@strain_routes.route("/<strain>", methods=['GET'])
def get_strain(strain):
    """
        Can query pickled strains dictionary to get information about a particular strain
    """

    return jsonify({"strain":pickle_dict[strain]})


@strain_routes.route('/data', methods=["GET", "POST"])
def data():
    """View all strains in database."""

    create_table(extract_data())
    strain = Strain.query.all()
    records = parse_records(strain)
    
    return render_template("data.html", records=records, message="Home Page")




