from database.database import db
from datetime import datetime
from base.base import BaseModel

class Room(BaseModel):
    __tablename__ = "room"

    room_name = db.Column(db.String(128),nullable=False,unique=True)
    connected_user_info = db.relationship("ConnectedUser",lazy=True)
    connected_robot_info = db.relationship("ConnectedRobot",lazy=True)

    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
