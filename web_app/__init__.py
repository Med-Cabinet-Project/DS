#web_app/__init__.py

import os
from flask import Flask
from dotenv import load_dotenv

from web_app.models import DB, migrate
from web_app.routes.strain_routes import strain_routes

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

def create_app():
    APP = Flask(__name__)
    APP.config["SECRET_KEY"] = SECRET_KEY

    APP.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(APP)
    migrate.init_app(APP, DB)

    APP.register_blueprint(strain_routes)

    return APP

if __name__ == '__main__':
    
    my_app = create_app()
    my_app.run(debug=True)
