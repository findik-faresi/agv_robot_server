from flask_socketio import leave_room, emit
from termcolor import colored

from models import ConnectedRobot, Robot
from database.database import db

from . import socketio

@socketio.on("leave_robot")
def leave_robot(payload):
    try:
        secret_key = payload.get("secret_key")
        serial_number = payload.get("serial_number")

        if not (serial_number and secret_key):
            emit("leave_robot", {"message":"Invalid data", "status":400}, room=serial_number)
            return

        robot = Robot.query.filter_by(serial_number=serial_number).first()
        if not robot:
            emit("leave_robot", {"message":"Robot not found", "status":404}, room=serial_number)
            return

        connected_robot = ConnectedRobot.query.filter_by(robot_id=robot.id).first()
        if not connected_robot:
            emit("leave_robot", {"message":"Record not found", "status":404}, room=serial_number)
            return
        else:
            connected_robot.connected = False
            db.session.commit()
            leave_room(room)

        emit("leave_robot", {"message":{"id":robot.id}, "status": 200}, room=serial_number)

    except Exception as e:
        print(colored(f"Error handling leave event: {str(e)}", "red", attrs=["bold"]))
        emit("leave_robot", {"message": "An error occurred while processing your request", "status": 500}, room=serial_number)
