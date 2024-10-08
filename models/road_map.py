from database.database import db
from datetime import datetime 
from base.base import BaseModel

class RoadMap(BaseModel):
    __tablename__ = "road_map"
    
    mission_id = db.Column(db.Integer, db.ForeignKey("mission.id"), nullable=False)

    qr_code_id = db.Column(db.Integer, db.ForeignKey("qr_code.id"))

    index = db.Column(db.Integer, nullable=False)
    reached = db.Column(db.Boolean, nullable=False,default=False)

    reached_time = db.Column(db.DateTime, nullable=True)   
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
