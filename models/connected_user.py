from datetime import datetime 
from database.database import db
from base.base import BaseModel

class ConnectedUser(BaseModel):
    __tablename__ = "connected_user"

    room_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    connected = db.Column(db.Boolean, nullable=False, default=True)
    internet_protocol = db.Column(db.String(16), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
