from flask import request
from flask import jsonify
from .DBConnection import get_connection
import psycopg2
import json
from .models import db, CarsModel


def hello():
    return " Rello World"


def create_room():
    CREATE_ROOMS_TABLE = (
        "CREATE TABLE IF NOT EXISTS public.rooms (id SERIAL PRIMARY KEY, name TEXT);"
    )

    INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"
    data = request.get_json()
    name = data["name"]
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(CREATE_ROOMS_TABLE)
    cursor.execute(INSERT_ROOM_RETURN_ID, (name,))
    connection.commit()
    room_id = cursor.fetchone()[0]
    return {"id": room_id, "message": f"{name} created."}


def read_room():
    Read_Room = ("SELECT * FROM public.rooms")
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute(Read_Room)
    doom = cursor.fetchall()
    jsonString = json.dumps(doom)
    return jsonString


def update_room():
    update_room = ("UPDATE public.rooms SET name=(%s) WHERE id=(%s);")
    data = request.get_json()
    Roomname = data["name"]
    Rid = data["id"]
    print(Rid, Roomname)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(update_room, (Roomname, Rid,))
    connection.commit()

    return "201"


def delete_room():
    delete_room = ("DELETE FROM public.rooms WHERE id = (%s);")
    data = request.get_json()
    Rid = data["id"]
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(delete_room, (Rid,))
    connection.commit()

    return "201"


def car_api():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = CarsModel(
                name=data['name'], model=data['model'], doors=data['doors'])
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


def update_car(car_id):
    car = CarsModel.query.get_or_404(car_id)
    if request.method == 'GET':
        response = {
            "name": car.name,
            "model": car.model,
            "doors": car.doors
        }
        return jsonify(response)
    elif request.method == 'PUT':
        data = request.get_json()
        print(data["name"])
        car.name = data["name"]
        car.model = data["model"]
        car.doors = data["doors"]
        db.session.add(car)
        db.session.commit()
        return {"message": f"car {car.name} successfully updated"}
    elif request.method == 'DELETE':
        db.session.delete(car)
        db.session.commit()
        return {"message": f"Car {car.name} successfully deleted."}
