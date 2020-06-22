#web_app/routes/strain_routes.py

from flask import Blueprint, render_template, flash, redirect
import requests
from web_app.models import DB, Strain, create_table, add_table, parse_records #get_records, add_records
from web_app.services.strains_service import API 


strain_routes = Blueprint("strain_routes", __name__)

@strain_routes.route('/', methods=["GET", "POST"])
def roots():
    """Add strains to db_strain."""

    add_table(create_table())
    strain = Strain.query.all()
    records = parse_records(strain)
    
    
    return render_template("form.html", records=records, message="Home Page")

@strain_routes.route('/refresh', methods=["GET", "POST"])
def refresh():
    """Add strains to db_strain."""

    add_table(create_table())
    strain = Strain.query.all()
    records = parse_records(strain)
    
    return render_template("refresh.html", records=records, message="Home Page")


