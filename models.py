from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import app
from .DBconfig import AlConfig

Mapp = app
URI = AlConfig()
Mapp.config['SQLALCHEMY_DATABASE_URI'] = URI
db = SQLAlchemy(Mapp)
migrate = Migrate(Mapp,db)
class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors