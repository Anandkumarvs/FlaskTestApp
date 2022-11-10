from . import create_app
from .services import create_room
from .services import hello
from .services import read_room
from .services import update_room
from .services import delete_room
from .models import db,CarsModel
from flask import request,Response
from .services import car_api
from .services import update_car
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
   return car_api()
@app.route('/cars/<car_id>',methods =['GET','PUT','DELETE'])
def updateCar(car_id):
    return update_car(car_id)
    
