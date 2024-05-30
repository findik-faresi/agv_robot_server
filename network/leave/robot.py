from flask_socketio import leave_room, emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import ConnectedRobotInfo, Robot
from database.database import db

@socketio.on("_10")
@jwt_required()
def _10(payload):
    if not Auth.jwt_authenticate():
        emit("_10", {"message":"Unauthorized","status":401})
        return

    secret_key = payload["secret_key"]
    serial_number = payload["serial_number"]

    if not (serial_number and secret_key):
        emit("_10", {"message":"Invalid data","status":400})
        return

    robot = Robot.query.filter_by(serial_number=serial_number).first()
    if not robot:
        emit("_10", {"message":"Robot not found","status":404})
        return

    connected_robot_info = ConnectedRobotInfo.query.filter_by(robot_id=robot.id).first()
    if not connected_robot_info:
        emit("_10", {"message":"Record not found","status":404})
        return
    else:
        connected_robot_info.connected = False
        leave_room(room)

    if room_name: 
        emit("_10", {"id":robot.id  , "status": 200}, room=room)
