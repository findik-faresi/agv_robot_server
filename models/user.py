from datetime import datetime 
from database.database import db
from base.base import BaseModel

class User(BaseModel):
    __tablename__ = "user"

    username = db.Column(db.String(128),nullable=False)
    password = db.Column(db.String(1024),nullable=False)
    role = db.Column(db.Integer,nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
    connected_user_info = db.relationship("ConnectedUserInfo",lazy=True)

