from flask import request
from .DBConnection import get_connection
import psycopg2
import json
def hello():
 return " Rello World"

def create_room():
    CREATE_ROOMS_TABLE = (
    "CREATE TABLE IF NOT EXISTS public.rooms (id SERIAL PRIMARY KEY, name TEXT);"
)

    INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"
    data = request.get_json()
    name = data ["name"]
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
    data=request.get_json()
    Roomname = data["name"]
    Rid= data["id"]
    print (Rid,Roomname)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(update_room,(Roomname,Rid,))
    connection.commit()
    
    return "201"

def delete_room():
    delete_room = ("DELETE FROM public.rooms WHERE id = (%s);")
    data=request.get_json()
    Rid= data["id"]
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(delete_room,(Rid,))
    connection.commit()
    
    return "201"