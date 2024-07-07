from flask_socketio import emit
from network import socketio
from models import QRCode

@socketio.on("_c2")
def _c2(payload):
    try:
        room = payload.get("room")
        data = payload.get("data")

        if not (room and data):
            emit("_sc2", {"message":"Invalid data","status":400}) 
            return

        qr_code = QRCode.query.filter_by(vertical_coordinate=data.get("vertical_coordinate"),horizontall_coordinate=data.get("horizontall_coordinate")).first()

        if not qr_code:
            qr_code = QRCode(data)
            db.session.add(qr_code)
            db.session.commit()

        emit("_sc2", {"message": data,"status":200}, room=room)

    except Exception as e:
        print(f"Error handling _c2 event: {str(e)}")
        emit("_sc2", {"message": "An error occurred while processing your request", "status": 500})
