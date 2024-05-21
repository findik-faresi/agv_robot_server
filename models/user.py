from database.database import db
from datetime import datetime 

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    
    role = db.Column(db.Integer, nullable=False)
    
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    connected_user_info = db.relationship("connected_user_info",lazy=True)
