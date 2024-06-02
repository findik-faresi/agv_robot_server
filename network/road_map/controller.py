from flask_socketio import emit
from network import socketio
from auth.jwt.jwt_auth import Auth
from flask_jwt_extended import jwt_required
from database.database import db
from models import RoadMap,Mission

@socketio.on("_c5")
@jwt_required()
def _c5(payload):
    try:
        if not Auth.jwt_authenticate():
            emit("_sc5", {"message":"Unauthorized","status":401})
            return

        room = payload.get("room")
        data = payload.get("data")

        if not(room and data):
            emit("_sc5", {"message":"Invalid data","status":400}) 
            return
        
        mission = Mission.query.filter_by(secret_key=data.get("secret_key")).first()
        if not mission:
            emit("_sc5", {"message":"Data not found","status":415}) 
            return

        road_map = RoadMap.query.filter_by(mission_id=mission.id,target_area=data.get("target_area")).first()
        if road_map:
            road_map.reached = data.get("reached")
            road_map.reached_time = data.get("reached_time")
            db.session.commit()
        
        else:
            emit("_sc5", {"message":"Data not found","status":415}) 
            return

        emit("_sc5", {"message":data,"status":200}, room=room)
    
    except Exception as e:
        print(f"Error handling _c5 event: {str(e)}")
        emit("_sc5", {"message": "An error occurred while processing your request", "status": 500})
