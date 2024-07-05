from flask_socketio import emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import RobotLocation
from database.database import db

@socketio.on("_c6")
def _c6(payload):
    try:
        room = payload.get("room")
        data = payload.get("message")

        if not (room and data):
            emit("_sc6", {"message":"Invalid data","status":400})
            return
        
        print(f"[+] Camera data : {data}")

        emit("_sc6", {"message": data,"status":200}, room=room)
        
    except Exception as e:
        print(f"Error handling camera event: {str(e)}")
        emit("_sc6", {"message": "An error occurred while processing your request", "status": 500})
