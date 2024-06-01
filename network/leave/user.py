from flask_socketio import leave_room, emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import ConnectedUser,User 
from database.database import db

@socketio.on("_00")
@jwt_required()
def _00(payload):
    if not Auth.jwt_authenticate():
        emit("_s00", {"message":"Unauthorized","status":401})
        return

    room = payload.get("room")
    id = payload.get("id")

    if not (id and room):
        emit("_s00", {"message":"Invalid data","status":400})
        return

    user = User.query.filter_by(id=user_id).first()
    if not user:
        emit("_s00", {"message":"Robot not found","status":404})
        return

    connected_user = ConnectedUser.query.filter_by(user_id=user.id).first()
    if not connected_user:
        emit("_s00", {"message":"Record not found","status":404})
        return
    else:
        connected_user.connected = False
        leave_room(room)
        db.session.commit()

    emit("_s00", {"message":{"id": user.id}, "status": 200}, room=room)
