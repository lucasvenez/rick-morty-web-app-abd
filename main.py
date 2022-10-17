from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

application = Flask(__name__)
application.config.from_object("config.Config")

db.init_app(application)

from index.routes import index_bp
application.register_blueprint(index_bp)

from model import *

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
