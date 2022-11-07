from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_application():

    application = Flask(__name__)
    application.config.from_object("config.Config")

    db.init_app(application)

    with application.app_context():
        db.drop_all()
        db.create_all()

    from index.routes import index_blueprint
    application.register_blueprint(index_blueprint)

    from character.routes import character_blueprint
    application.register_blueprint(character_blueprint, url_prefix="/character")

    return application

from model import *

if __name__ == "__main__":
    application = create_application()
    application.run(host="0.0.0.0", port=5000)
