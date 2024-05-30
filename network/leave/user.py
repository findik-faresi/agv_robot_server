from flask_socketio import leave_room, emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import ConnectedUserInfo,User 
from database.database import db

@socketio.on("_00")
@jwt_required()
def _00(payload):
    if not Auth.jwt_authenticate():
        emit("_00", {"message":"Unauthorized","status":401})
        return

    room_name = payload["room_name"]
    user_id = payload["user_id"]

    if not (user_id and room_name):
        emit("_00", {"message":"Invalid data","status":400})
        return

    user = User.query.filter_by(id=user_id).first()
    if not user:
        emit("_00", {"message":"Robot not found","status":404})
        return

    connected_user_info = ConnectedUserInfo.query.filter_by(user_id=user.id).first()
    if not connected_user_info:
        emit("_00", {"message":"Record not found","status":404})
        return
    else:
        connected_user_info.connected = False
        leave_room(room)

    if room_name: 
        emit("_00", {"id":user.id  , "status": 200}, room=room)
