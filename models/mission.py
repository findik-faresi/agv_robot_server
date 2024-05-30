from datetime import datetime 
from database.database import db
from base.base import BaseModel

class Mission(BaseModel):
    __tablename__ = "mission"

    robot_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)
    mission_end_time = db.Column(db.DateTime, nullable=False)  
    secret_key = db.Column(db.String(16), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   

    turn_point = db.relationship("TurnPoint",lazy=True)
    qr_code_datal = db.relationship("QRCodeData",lazy=True)
    road_map = db.relationship("RoadMap",lazy=True)
