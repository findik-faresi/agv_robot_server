from flask_socketio import join_room, emit
from models import Room,Robot,ConnectedRobotInfo
from database.database import db
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from flask import request

@socketio.on("_11")
@jwt_required()
def _11(payload):
    if not Auth.jwt_authenticate():
        emit("_11", {"message":"Unauthorized","status":401})
        return

    serial_number = payload.get("serial_number")
    secret_key = payload.get("secret_key")
    ip_address = request.remote_addr 

    if not (serial_number and secret_key and ip_address):
        emit("_11", {"message":"Invalid data","status":400})
        return

    robot = Robot.query.filter_by(serial_number=serial_number).first()
    if not robot:
        robot = Robot(serial_number=serial_number, secret_key=secret_key)
        db.session.add(robot)
        db.session.commit()

    room = Room.query.filter_by(room_name=serial_number).first()
    if not room:
        room = Room(room_name=serial_number)
        db.session.add(room)
        db.session.commit()

    connected_robot_info = ConnectedRobotInfo.query.filter_by(robot_id=robot.id).first()
    if not connected_robot_info:
        connected_robot_info = ConnectedRobotInfo(
            room_id=room.id,
            robot_id=robot.id,
            connected=True,
            internet_protocol=ip_address
        )
    else:
        connected_robot_info.connected = True 

    db.session.add(connected_robot_info)
    db.session.commit()
    
    print(f"[+] {secret_key}") 
    
    join_room(serial_number)
    emit("_11", {"id": robot.id, "status": 200}, room=serial_number)
