from flask_socketio import join_room, emit
from models import Room,Robot,ConnectedRobot
from database.database import db
from network import socketio
from flask import request
from werkzeug.security import check_password_hash

@socketio.on("_11")
def connect(payload):
    try:
        serial_number = payload.get("serial_number")
        secret_key = payload.get("secret_key")
        ip_address = request.remote_addr 

        if not (serial_number and secret_key and ip_address):
            emit("_s11", {"message":"Invalid data","status":400})
            return

        robot = Robot.query.filter_by(serial_number=serial_number).first()

        if not robot:
            emit("_s11", {"message":"Record not found","status":415})
            return

        if check_password_hash(robot.secret_key,serial_number):
            emit("_s11", {"message":" Unauthorized not found","status":401})
            return 

        room = Room.query.filter_by(room_name=serial_number).first()

        if not room:
            room = Room(room_name=serial_number)
            db.session.add(room)

        connected_robot = ConnectedRobot.query.filter_by(robot_id=robot.id).first()
        if not connected_robot:
            connected_robot = ConnectedRobot(
                room_id=room.id,
                robot_id=robot.id,
                connected=True,
                internet_protocol=ip_address
            )
            db.session.add(connected_robot)
        else:
            connected_robot.connected = True 
            if connected_robot.internet_protocol != ip_address:
                connected_robot.internet_protocol = ip_address

        db.session.commit()
        
        join_room(serial_number)

        emit("_s11", {"message":{"id": serial_number}, "status": 200}, room=serial_number)

        print(f"[+] Robot connected to server {serial_number}.")
    except Exception as e:
        print(f"Error handling connection event: {str(e)}")
        emit("_s11", {"message": "An error occurred while processing your request", "status": 500})
