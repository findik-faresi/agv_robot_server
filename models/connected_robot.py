from database.database import db
from datetime import datetime 
from base.base import BaseModel

class ConnectedRobot(BaseModel):
    __tablename__ = "connected_robot"
    
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)
    robot_id = db.Column(db.Integer, db.ForeignKey("robot.id"), nullable=False)

    connected = db.Column(db.Boolean, nullable=False, default=True)
    internet_protocol = db.Column(db.String(16), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
