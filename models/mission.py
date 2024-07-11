from datetime import datetime 
from database.database import db
from base.base import BaseModel

class Mission(BaseModel):
    __tablename__ = "mission"

    robot_id = db.Column(db.Integer, db.ForeignKey("robot.id"), nullable=False)

    mission_end_time = db.Column(db.DateTime, nullable=True)  

    active = db.Column(db.Boolean, nullable=False, default=True)

    is_completed = db.Column(db.Boolean, nullable=False, default=False)

    rank = db.Column(db.Integer, nullable=False ,default=0)
    _type = db.Column(db.String(1), nullable=False ,default="0")
    
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    road_map = db.relationship("RoadMap",lazy=True)
     
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
