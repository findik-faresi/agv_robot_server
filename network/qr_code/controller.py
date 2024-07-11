from flask_socketio import emit
from network import socketio
from models import QRCode

@socketio.on("_c2")
def _c2(payload):
    try:
        room_name = payload.get("room_name")
        data = payload.get("message")

        if not (data and room_name):
            emit("_sc2", {"message":"Invalid data","status":400},room=room_name) 
            return

        qr_code = QRCode.query.filter_by(area_name=data.get("area_name")).first()

        if not qr_code:
            qr_code = QRCode(data)
            db.session.add(qr_code)
            db.session.commit()

        emit("_sc2", {"message": data,"status":200}, room=room_name)

    except Exception as e:
        print(f"Error handling _c2 event: {str(e)}")
        emit("_sc2", {"message": "An error occurred while processing your request", "status": 500},room=room_name)
