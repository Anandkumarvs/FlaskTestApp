from . import create_app
from .services import create_room
from .services import hello
from .services import read_room
from .services import update_room
from .services import delete_room
from .models import db,CarsModel
from flask import request,Response

app = create_app()

@app.get("/")
def Hi():
    return hello()

@app.post("/api/createRoom")
def Create_Rooms():
    return create_room()

@app.get("/api/getRoom")
def GetRoom():
    return read_room()

@app.put("/api/updateRoom")
def UpdateRoom():
    return update_room()

@app.post("/api/deleteRoom")
def DeleteRoom():
    return delete_room()
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
