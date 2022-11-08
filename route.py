from . import create_app
from .services import create_room
from .services import hello
from .services import read_room
from .services import update_room
from .services import delete_room
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