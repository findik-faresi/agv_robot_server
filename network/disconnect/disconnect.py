from flask_socketio import leave_room, emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import ConnectedRobot, ConnectedUser, Robot
from database.database import db
from flask import request

@socketio.on("disconnect")
def handle_disconnect():
    try:
        ip_address = request.remote_addr

        connected_user = ConnectedUser.query.filter_by(internet_protocol=ip_address).first()
        if connected_user:
            connected_user.connected = False
            db.session.commit()
            return 

        connected_robot = ConnectedRobot.query.filter_by(internet_protocol=ip_address).first()
        if connected_robot:
            connected_robot.connected = False
            db.session.commit()
    except Exception as e:
        # Log the error or handle it as needed
        print(f"Error handling disconnect: {str(e)}")
