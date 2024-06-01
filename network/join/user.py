from flask_socketio import join_room, emit
from models import Room,ConnectedUserInfo,User
from database.database import db
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required

@socketio.on("_01")
@jwt_required()
def _01(payload):
    if not Auth.jwt_authenticate():
        emit("_s01", {"message":"Unauthorized","status":401})
        return

    room = payload.get("room")
    user_id = payload.get("user_id")
    ip_address = payload.get("ip_address")

    if not (room_name and user_id and ip_address):
        emit("_s01", {"message":"Invalid data","status":400})
        return

    user = User.query.filter_by(id=user_id).first()
    if not user:
        emit("_s01", {"message":"Record not found","status":404})
        return

    room = Room.query.filter_by(room_name=room_name).first()
    if not room:
        emit("_s01", {"message":"Record not found","status":404})
        return

    connected_user_info = ConnectedUserInfo.query.filter_by(user_id=user.id).first()
    if not connected_user_info: 
        connected_user_info = ConnectedUserInfo(
            room_id=room.id,
            user_id=user_id,
            connected=True,
            internet_protocol=ip_address
        )
        db.session.add(connected_user_info)
    else:
        connected_user_info.connected = True
        if connected_user_info.internet_protocol != ip_address:
            connected_user_info.internet_protocol = ip_address

    db.session.commit()
    
    join_room(room_name)
    emit("_s01", {"message":{"id": user.id}, "status": 200}, room=room)
