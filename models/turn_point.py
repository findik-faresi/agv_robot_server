from database.database import db
from datetime import datetime 
from base.base import BaseModel

class TurnPoint(BaseModel):
    __tablename__ = "turn_point"

    mission_id = db.Column(db.Integer, db.ForeignKey("mission.id"), nullable=False)

    distance_traveled = db.Column(db.Float,nullable=False)
    traveled_direction = db.Column(db.Integer, nullable=False)

    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
