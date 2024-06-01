from flask_socketio import leave_room, emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import ConnectedRobot, Robot
from database.database import db

@socketio.on("_10")
@jwt_required()
def _10(payload):
    if not Auth.jwt_authenticate():
        emit("_s10", {"message":"Unauthorized","status":401})
        return

    secret_key = payload.get("secret_key")
    serial_number = payload.get("serial_number")

    if not (serial_number and secret_key):
        emit("_s10", {"message":"Invalid data","status":400})
        return

    robot = Robot.query.filter_by(serial_number=serial_number).first()
    if not robot:
        emit("_s10", {"message":"Robot not found","status":404})
        return

    connected_robot = ConnectedRobot.query.filter_by(robot_id=robot.id).first()
    if not connected_robot:
        emit("_s10", {"message":"Record not found","status":404})
        return
    else:
        connected_robot.connected = False
        db.session.commit()
        leave_room(room)

    emit("_s10", {"message":{"id":robot.id}, "status": 200}, room=room)
