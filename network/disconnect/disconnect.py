from flask_socketio import leave_room, emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import ConnectedRobotInfo,ConnectedUserInfo,Robot
from database.database import db
from flask_jwt_extended import get_jwt_identity

@socketio.on("disconnect")
@jwt_required()
def handle_disconnect():
    identity = get_jwt_identity()
    if type(identity) == int:
        connected_user = ConnectedUserInfo.query.filter_by(user_id=identity).first() 
        if connected_user:
            connected_user.connected = False
            db.session.commit()
    else:
        robot = Robot.query.filter_by(serial_number=identity).first()
        if robot:
            connected_robot = ConnectedRobotInfo.query.filter_by(robot_id=robot.id).first()
            if connected_robot:
                connected_robot.connected = False
                db.session.commit()
