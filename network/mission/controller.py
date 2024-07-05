from flask_socketio import emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from database.database import db
from models import Mission,RoadMap

@socketio.on("_c1")
def _c1(payload):
    try:
        room = payload.get("room")
        data = payload.get("message")

        if not (room and data):
            emit("_sc1", {"message":"Invalid data","status":400}) 
            return

        mission = Mission.from_dict(data.get("mission"))

        db.session.add(mission)
        db.session.flush()

        for d in data.get("road_maps"):
            d["mission_id"] = mission.id
            road_map = RoadMap.from_dict(d)
            db.session.add(road_map)

        db.session.commit()

        emit("_sc1", {"message": data,"status":200}, room=room)

    except Exception as e:
        print(f"Error handling _c1 event: {str(e)}")
        emit("_sc1", {"message": "An error occurred while processing your request", "status": 500})
