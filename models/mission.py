from datetime import datetime 
from database.database import db
from base.base import BaseModel

class Mission(BaseModel):
    __tablename__ = "mission"

    robot_id = db.Column(db.Integer, db.ForeignKey("robot.id"), nullable=False)
    mission_end_time = db.Column(db.DateTime, nullable=False)  
    secret_key = db.Column(db.String(128), nullable=False,unique=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    turn_point = db.relationship("TurnPoint",lazy=True)
    road_map = db.relationship("RoadMap",lazy=True)
  
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
