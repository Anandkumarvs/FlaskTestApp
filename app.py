import os
from dotenv import load_dotenv
from . import create_app
from . import DBConnection
from . import route
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
load_dotenv()
app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://Anand:AnandSql@localhost:5432/cars_api"
db = SQLAlchemy(app)
migrate = Migrate(app,db)

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
@app.route('/cars', methods=['POST', 'GET'])
def handle_cars():  
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                new_car = CarsModel(name=data['name'], model=data['model'], doors=data['doors'])
                db.session.add(new_car)
                db.session.commit()
                return {"message": f"car {new_car.name} has been created successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}

        elif request.method == 'GET':
                cars = CarsModel.query.all()
                results = [
                     {
                      "name": car.name,
                       "model": car.model,
                        "doors": car.doors
                          } for car in cars]

        return {"count": len(results), "cars": results}
@app.route('/cars/<car_id>',methods =['GET','PUT','DELETE'])
def updateCar(car_id):
    car = CarsModel.query.get_or_404(car_id)
    if request.method =='GET':
        response = {
            "name": car.name,
            "model": car.model,
            "doors": car.doors
        }
        return response
    elif request.method=='PUT':
        data = request.get_json()
        print (data["name"])
        car.name= data["name"]
        car.model = data["model"]
        car.doors = data["doors"]
        db.session.add(car)
        db.session.commit()
        return {"message": f"car {car.name} successfully updated"}
    elif request.method=='DELETE':
        db.session.delete(car)
        db.session.commit()
        return {"message": f"Car {car.name} successfully deleted."}

DBConnection.connect()
