from flask_socketio import emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import RobotLocation
from database.database import db

@socketio.on("_c0")
def _c0(payload):
    try:
        room = payload.get("room")
        data = payload.get("message")

        if not (room and data):
            emit("_sc0", {"message":"Invalid data","status":400})
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

        emit("_sc0", {"message": data,"status":200}, room=room)
        
    except Exception as e:
        print(f"Error handling _c0 event: {str(e)}")
        emit("_sc0", {"message": "An error occurred while processing your request", "status": 500})
