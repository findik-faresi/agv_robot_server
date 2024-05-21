from datetime import datetime 
from database.database import db

class Mission(db.Model):
    __tablename__ = "mission"

    id = db.Column(db.Integer, primary_key=True)
    robot_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)
    mission_end_time = db.Column(db.DateTime, nullable=False)  
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   

    turn_point = db.relationship("turn_point",lazy=True)
    qr_code_datal = db.relationship("qr_code_data",lazy=True)
    road_map = db.relationship("road_map",lazy=True)
