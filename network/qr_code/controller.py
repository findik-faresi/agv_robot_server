from flask_socketio import emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from models import QRCode

@socketio.on("_c2")
@jwt_required()
def _c2(payload):
    if not Auth.jwt_authenticate():
        emit("_sc2", {"message":"Unauthorized","status":401})
        return

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
