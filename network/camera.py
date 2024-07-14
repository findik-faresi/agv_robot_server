from flask_socketio import emit
from termcolor import colored

from models import RobotLocation
from database.database import db

from . import socketio

@socketio.on("camera")
def camera(payload):
    try:
        room_name = payload.get("room_name")
        data = payload.get("message")

        if not (room_name and data):
            emit("camera", {"message":"Invalid data", "status":400}, room=room_name)
            return

        emit("camera", {"message": data, "status":200}, room=room_name)
        
    except Exception as e:
        print(colored(f"Error handling camera event: {str(e)}", "red", attrs=["bold"]))
        emit("camera", {"message": "An error occurred while processing your request", "status": 500}, room=room_name)
