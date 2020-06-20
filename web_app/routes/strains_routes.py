
from flask import Blueprint, render_template, flash, redirect
import requests
from web_app.models import db, Strain, get_records, add_records, parse_records
from web_app.services.strains_service import API

strain_routes = Blueprint("strain_routes", __name__)

@aq_routes.route('/home', methods=["GET", "POST"])
def root():
    """Base view."""
    #`Record` objects that have `value` greater or equal to 10.
    add_records(get_records())

    records = Record.query.filter(Record.value >= 10).all()
    print(records)

    return render_template("form.html", records=records, message="Home Page")

@aq_routes.route('/refresh')
def refresh():
    """Replace existing data with data from OpenAQ."""
    DB.drop_all()
    DB.create_all()

    # add new records
    add_records(get_records())
    records = Record.query.filter(Record.value >=10).all()
    
    print(records)

    flash(f"'Data refreshed!", "success") # "danger" "warning"
    return render_template("refresh.html", records=records)