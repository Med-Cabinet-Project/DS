#web_app/routes/strain_routes.py

from flask import Blueprint, render_template, flash, redirect, jsonify
import requests
import pickle
import os
from web_app.models import DB, Strain, extract_data, create_table, parse_records
from web_app.services.strains_service import API 


strain_routes = Blueprint("strain_routes", __name__)



@strain_routes.route("/<strain>", methods=['GET'])
def root(strain):
    """
        Root of the app.
    """

    PICKLE_FILEPATH = os.path.join(os.path.dirname(__file__),"..", "stats_model", "strains.pkl")
    pickle_dict = pickle.load(open(PICKLE_FILEPATH, "rb"))

    return jsonify({"strain":pickle_dict[strain]})




@strain_routes.route('/data', methods=["GET", "POST"])
def roots():
    """Base view."""

    create_table(extract_data())
    strain = Strain.query.all()
    records = parse_records(strain)
    
    return render_template("data.html", records=records, message="Home Page")




