from flask_socketio import emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import TurnPoint,Mission

@socketio.on("_c4")
@jwt_required()
def _c4(payload):
    try:
        if not Auth.jwt_authenticate():
            emit("_sc4", {"message":"Unauthorized","status":401})
            return

        room = payload.get("room")
        data = payload.get("data")

        if not (room and data):
            emit("_sc4", {"message":"Invalid data","status":400}) 
            return

        mission = Mission.query.filter_by(secret_key=data.get("secret_key"))
        if not mission:
            emit("_sc4", {"message":"Data not found","status":415}) 
            return

        emit("_sc4", {"data": data,"status":200}, room=room)
    
    except Exception as e:
        print(f"Error handling _c4 event: {str(e)}")
        emit("_sc4", {"message": "An error occurred while processing your request", "status": 500})
