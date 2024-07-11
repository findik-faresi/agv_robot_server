from flask_socketio import emit
from network import socketio
from database.database import db
from models import RoadMap ,Mission ,QRCode

@socketio.on("_c5")
def _c5(payload):
    try:
        room_name = payload.get("room_name")
        data = payload.get("message")

        if not(data and room_name):
            emit("_sc5", {"message":"Invalid data","status":400}, room=room_name) 
            return

        mission = Mission.query.filter_by(mission_id=data.get("id")).first()

        if not mission:
            emit("_sc5", {"message":"Data not found","status":415}, room=room_name) 
            return

        if not mission.activate:
            emit("_sc5", {"message":"Mission is not active","status":415}, room=room_name) 
            return

        road_map = RoadMap.query.filter_by(
                mission_id=data.get("id"),
                index=data.get("index"),
                qr_code_id=data.get("qr_code_id")
        ).first()

        if road_map:
            road_map.reached = data.get("reached")
            road_map.reached_time = data.get("reached_time")
            db.session.commit()
        else:
            emit("_sc5", {"message":"Data not found","status":415}, room=room_name) 
            return

        r = RoadMap.query.filter_by(
                mission_id=data.get("id"),
                reached=False
        ).first()

        if not r:
            mission.is_completed = True
            mission.active = False
            db.session.commit()

        emit("_sc5", {"message":data,"status":200}, room=room_name)
    except Exception as e:
        print(f"Error handling road_map event: {str(e)}")
        emit("_sc5", {"message": "An error occurred while processing your request", "status": 500},room=room_name)
