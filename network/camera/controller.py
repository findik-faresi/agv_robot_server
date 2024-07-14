from flask_socketio import emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import RobotLocation
from database.database import db
from termcolor import colored

@socketio.on("_c6")
def _c6(payload):
    try:
        room_name = payload.get("room_name")
        data = payload.get("message")

        if not (room_name and data):
            emit("_sc6", {"message":"Invalid data", "status":400}, room=room_name)
            return

        emit("_sc6", {"message": data, "status":200}, room=room_name)
        
    except Exception as e:
        print(colored(f"Error handling camera event: {str(e)}", "red", attrs=["bold"]))
        emit("_sc6", {"message": "An error occurred while processing your request", "status": 500}, room=room_name)
