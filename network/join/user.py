from flask_socketio import join_room, emit
from models import Room,ConnectedUser,User
from database.database import db
from network import socketio
from flask import request
from termcolor import colored

@socketio.on("_01")
def _01(payload):
    try:
        room_name = payload.get("room_name")
        user_id = payload.get("user_id")
        ip_address = request.remote_addr 

        if not (room_name and user_id and ip_address):
            emit("_s01", {"message":"Invalid data","status":400})
            return

        user = User.query.filter_by(id=user_id).first()
        if not user:
            emit("_s01", {"message":"Record not found","status":404})
            return

        room = Room.query.filter_by(room_name=room_name).first()

        if not room:
            room = Room(room_name=room_name)
            db.session.add(room)

        connected_user = ConnectedUser.query.filter_by(user_id=user.id).first()
        if not connected_user: 
            connected_user = ConnectedUser(
                room_id=room.id,
                user_id=user_id,
                connected=True,
                internet_protocol=ip_address
            )
            db.session.add(connected_user)
        else:
            connected_user.connected = True
            if connected_user.internet_protocol != ip_address:
                connected_user.internet_protocol = ip_address

        db.session.commit()
        
        print(colored(f"[+] {user.username} connected to : {room_name}", "green"))

        join_room(room_name)
        emit("_s01", {"message":{"id": user.id}, "status": 200}, room=room_name)
    except Exception as e:
        print(colored(f"[-] Error handling join event: {str(e)}", "red"))
        emit("_s01", {"message": "An error occurred while processing your request", "status": 500})
