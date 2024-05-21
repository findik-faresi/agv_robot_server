from database.database import db
from datetime import datetime

class Room(db.Model):
    __tablename__ = "room"

    id = db.Column(db.Integer, primary_key=True)

    room_name = db.Column(db.String(128),nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    connected_user_info = db.relationship("connected_user_info",lazy=True)

    connected_robot_info = db.relationship("connected_robot_info",lazy=True)
