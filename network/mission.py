from flask_socketio import emit
from termcolor import colored

from database.database import db
from models import Mission, RoadMap, QRCode, Robot

from . import socketio

@socketio.on("mission")
def mission(payload):
    try:
        room_name = payload.get("room_name")
        data = payload.get("message")

        print(colored(f"[+] Mission : {data}", "green", attrs=["bold"]))

        if not (data and room_name):
            emit("mission", {"message":"Invalid data", "status":400}, room=room_name) 
            return
        
        robot = Robot.query.filter_by(serial_number=room_name).first()

        if not robot:
            emit("mission", {"message":"Record not found", "status":415}, room=room_name)
            return
         
        mission = Mission(robot_id=robot.id)

        db.session.add(mission)
        db.session.flush()

        for d in data:
            qr_code = QRCode.query.filter_by(area_name=d.get("area_name")).first()
            
            if not qr_code:
                emit("mission", {"message":"Qr code not found", "status":400}, room=room_name) 
                return

            r = RoadMap(
                mission_id = mission.id,
                qr_code_id = qr_code.id,
                index = d.get("index"),
            )

            db.session.add(r)

        db.session.commit()

        emit("mission", {"message":data, "status":200}, room=room_name)
    except Exception as e:
        print(colored(f"Error handling mission event: {str(e)}", "red", attrs=["bold"]))
        emit("mission", {"message": "An error occurred while processing your request", "status": 500}, room=room_name)
