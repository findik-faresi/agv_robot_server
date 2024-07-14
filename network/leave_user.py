from flask_socketio import leave_room, emit
from termcolor import colored

from models import ConnectedUser,User 
from database.database import db

from . import socketio

@socketio.on("leave_user")
def leave_user(payload):
    try:
        room_name = payload.get("room_name")
        id = payload.get("id")

        if not (id and room_name):
            emit("leave_user", {"message":"Invalid data", "status":400}, room=room_name)
            return

        user = User.query.filter_by(id=user_id).first()
        if not user:
            emit("leave_user", {"message":"Robot not found", "status":404}, room=room_name)
            return

        connected_user = ConnectedUser.query.filter_by(user_id=user.id).first()
        if not connected_user:
            emit("leave_user", {"message":"Record not found", "status":404}, room=room_name)
            return
        else:
            connected_user.connected = False
            leave_room(room_name)
            db.session.commit()

        emit("leave_user", {"message":{"id": user.id}, "status": 200}, room=room_name)

    except Exception as e:
        print(colored(f"Error handling leave event: {str(e)}", "red", attrs=["bold"]))
        emit("leave_user", {"message": "An error occurred while processing your request", "status": 500}, room=room_name)
