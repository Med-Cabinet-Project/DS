import os
from flask import Flask
from dotenv import load_dotenv

from web_app.models import db, migrate
from web_app.routes.strain_routes import strain_routes

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(strain_routes)

    return app



if __name__ == '__main__':
    
    my_app = create_app()
    my_app.run(debug=True)
