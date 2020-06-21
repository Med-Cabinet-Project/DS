#web_app/routes/strain_routes.py

from flask import Blueprint, render_template, flash, redirect
import requests
from web_app.models import DB, Strain, get_records, add_records
from web_app.services.strains_service import API 


strain_routes = Blueprint("strain_routes", __name__)

@strain_routes.route('/', methods=["GET", "POST"])
def roots():
    """Add strains to db_strain."""

    add_records(get_records())

    records = Strain.query.all()
    print(records)

    return render_template("form.html", records=records, message="Home Page")

@strain_routes.route('/refresh')
def refresh():
    """Replace existing data with data from OpenAQ."""
    DB.drop_all()
    DB.create_all()

    # add new records
    add_records(get_records())
    records = Strain.query.all()
    
    print(records)

    flash(f"'Data refreshed!", "success") # "danger" "warning"
    return render_template("refresh.html", records=records)

