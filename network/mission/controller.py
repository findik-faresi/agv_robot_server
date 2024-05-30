from flask_socketio import emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required

@socketio.on("_c1")
@jwt_required()
def _c1(payload):
    if not Auth.jwt_authenticate():
        emit("_c1", {"message":"Unauthorized","status":401})
        return

    room_name = payload["room_name"]
    data = payload["data"]

    if not (room_name and data):
        emit("_c1", {"message":"Invalid data","status":400}) 
        return

    emit("_c1", {"data": data,"status":200}, room=room_name)
