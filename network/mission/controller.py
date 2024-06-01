from flask_socketio import emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from database.database import db
from models import Mission,RoadMap

@socketio.on("_c1")
@jwt_required()
def _c1(payload):
    if not Auth.jwt_authenticate():
        emit("_sc1", {"message":"Unauthorized","status":401})
        return

    room = payload.get("room")
    data = payload.get("data")

    if not (room and data):
        emit("_sc1", {"message":"Invalid data","status":400}) 
        return

    mission = Mission.from_dict(data.get("M"))

    db.session.add(mission)
    db.session.flush()

    for d in data.get("R"):
        d["mission_id"] = mission.id
        road_map = RoadMap.from_dict(d)
        db.session.add(road_map)

    db.session.commit()

    emit("_sc1", {"message": data,"status":200}, room=room)
