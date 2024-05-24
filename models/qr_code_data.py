from database.database import db
from datetime import datetime 
from base.base import BaseModel

class QRCodeData(BaseModel):
    __tablename__ = "qr_code_data"

    mission_id = db.Column(db.Integer, db.ForeignKey("mission.id"), nullable=False)
    vertical_coordinate = db.Column(db.Float, nullable=False)
    horizontall_coordinate = db.Column(db.Float,nullable=False)
    area_name = db.Column(db.String(32),nullable=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
