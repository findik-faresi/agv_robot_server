from flask_socketio import emit
from network import socketio
from database.database import db
from models import Mission ,RoadMap ,QRCode

@socketio.on("_c1")
def _c1(payload):
    try:
        room_name = payload.get("room_name")
        data = payload.get("message")

        if not (room_name and data):
            emit("_sc1", {"message":"Invalid data","status":400}) 
            return

        mission = Mission.from_dict(data.get("mission"))

        db.session.add(mission)
        db.session.flush()

        for d in data.get("road_maps"):
            d["mission_id"] = mission.id

            qr_code = QRCode.query.filter_by(area_name=d.get("area_name")).first()
            
            if not qr_code:
                emit("_sc1", {"message":"Invalid data","status":400}) 
                return
            
            d["qr_code_id"] = qr_code_id

            road_map = RoadMap.from_dict(d)
            db.session.add(road_map)

        db.session.commit()

        emit("_sc1", {"message": data,"status":200}, room=room_name)
    except Exception as e:
        print(f"Error handling _c1 event: {str(e)}")
        emit("_sc1", {"message": "An error occurred while processing your request", "status": 500})
