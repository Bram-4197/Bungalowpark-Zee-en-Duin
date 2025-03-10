from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()


class Bungalow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    aantalPersonen = db.Column(db.Integer, nullable=False)
    prijs = db.Column(db.Float, nullable=False)
    fileLocation = db.Column(db.String(300), nullable=True)

