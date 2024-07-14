from flask_socketio import emit
from termcolor import colored

from models import RobotLocation
from database.database import db

from . import socketio

@socketio.on("location")
def location(payload):
    try:
        room_name = payload.get("room_name")
        data = payload.get("message")

        if not (room and data):
            emit("location", {"message":"Invalid data", "status":400}, room=room_name)
            return

        robot_location = RobotLocation.query.filter_by(mission_id=data.get("mission_id")).first()
        if not robot_location:
            robot_location = RobotLocation.from_dict(data)
        else:
            robot_location.distance_traveled = data.get("distance_traveled")
            if robot_location.traveled_direction != data.get("traveled_direction"):
                robot_location.traveled_direction = data.get("traveled_direction") 

        db.session.add(robot_location)
        db.session.commit()

        emit("location", {"message": data,"status":200}, room=room_name)
        
    except Exception as e:
        print(colored(f"Error handling location event: {str(e)}", "red", attrs=["bold"]))
        emit("location", {"message": "An error occurred while processing your request", "status": 500}, room=room_name)
