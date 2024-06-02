from flask_socketio import leave_room, emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import ConnectedRobot, ConnectedUser, Robot
from database.database import db
from flask_jwt_extended import get_jwt_identity

@socketio.on("disconnect")
@jwt_required()
def handle_disconnect():
    try:
        identity = get_jwt_identity()
        if type(identity) == int:
            connected_user = ConnectedUser.query.filter_by(user_id=identity).first()
            if connected_user:
                connected_user.connected = False
                db.session.commit()
        else:
            robot = Robot.query.filter_by(serial_number=identity).first()
            if robot:
                connected_robot = ConnectedRobot.query.filter_by(robot_id=robot.id).first()
                if connected_robot:
                    connected_robot.connected = False
                    db.session.commit()
    except Exception as e:
        # Log the error or handle it as needed
        print(f"Error handling disconnect: {str(e)}")
