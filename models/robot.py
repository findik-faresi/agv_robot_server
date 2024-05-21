from datetime import datetime 
from database.database import db

class Robot(db.Model):
    __tablename__ = "robot"

    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(16),nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
    connected_robot_info = db.relationship("connected_robot_info",lazy=True)
