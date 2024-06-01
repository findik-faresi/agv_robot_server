from database.database import db
from datetime import datetime 
from base.base import BaseModel

class TurnPoint(BaseModel):
    __tablename__ = "turn_point"

    mission_id = db.Column(db.Integer, db.ForeignKey("mission.id"), nullable=False)

    horizontall_coordinate = db.Column(db.Float,nullable=False)
    vertical_coordinate = db.Column(db.Integer, nullable=False)

    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
