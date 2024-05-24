from datetime import datetime 
from database.database import db
from base.base import BaseModel

class Robot(BaseModel):
    __tablename__ = "robot"

    serial_number = db.Column(db.String(16),nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
    connected_robot_info = db.relationship("ConnectedRobotInfo",lazy=True)
