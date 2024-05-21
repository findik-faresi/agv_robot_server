from datetime import datetime 
from database.database import db

class ConnectedUserInfo(db.Model):
    __tablename__ = "connected_user_info"

    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    internet_protocol = db.Column(db.String(16), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
