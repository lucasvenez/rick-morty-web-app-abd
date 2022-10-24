from datetime import datetime
from main import db


class Character(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    created = db.Column(db.String(30), nullable=False, default=str(datetime.utcnow()))
    gender = db.Column(db.String(10), nullable=True)
    status = db.Column(db.String(10), nullable=True)
    type = db.Column(db.String(10), nullable=True)
