from flask_socketio import emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import RobotLocation
from database.database import db

@socketio.on("_c0")
@jwt_required()
def _c0(payload):
    if not Auth.jwt_authenticate():
        emit("_sc0", {"message":"Unauthorized","status":401})
        return

    room = payload.get("room")
    data = payload.get("data")

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
