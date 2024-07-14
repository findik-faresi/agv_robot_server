from flask_socketio import emit
from . import socketio
from models import QRCode
from termcolor import colored

@socketio.on("qr_code")
def qr_code(payload):
    try:
        room_name = payload.get("room_name")
        data = payload.get("message")

        if not (data and room_name):
            emit("qr_code", {"message":"Invalid data","status":400}, room=room_name) 
            return

        qr_code = QRCode.query.filter_by(area_name=data.get("area_name")).first()

        if not qr_code:
            qr_code = QRCode(data)
            db.session.add(qr_code)
            db.session.commit()

        emit("qr_code", {"message": data,"status":200}, room=room_name)

    except Exception as e:
        print(colored(f"Error handling qr code event: {str(e)}", "red", attrs=["bold"]))
        emit("qr_code", {"message": "An error occurred while processing your request", "status": 500}, room=room_name)
