from flask_socketio import leave_room, emit
from flask import request
from termcolor import colored

from models import ConnectedRobot, ConnectedUser, Robot
from database.database import db

from . import socketio

@socketio.on("disconnect")
def disconnect():
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
        print(colored(f"[-] Error handling disconnect event: {str(e)}.", "red", attrs=["bold"]))
