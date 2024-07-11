from database.database import db
from datetime import datetime 
from base.base import BaseModel

class QRCode(BaseModel):
    __tablename__ = "qr_code"

    robot_id = db.Column(db.Integer, db.ForeignKey("robot.id"), nullable=False)

    vertical_coordinate = db.Column(db.Float, nullable=False)
    horizontal_coordinate = db.Column(db.Float,nullable=False)

    area_name = db.Column(db.String(4),nullable=True,unique=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   

    road_map = db.relationship("RoadMap",lazy=True)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
