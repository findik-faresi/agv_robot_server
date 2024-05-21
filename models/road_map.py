from database.database import db
from datetime import datetime 

class RoadMap(db.Model):
    __tablename__ = "road_map"

    id = db.Column(db.Integer, primary_key=True)
    
    robot_id = db.Column(db.Integer, db.ForeignKey("robot.id"), nullable=False)
    target_area = db.Column(db.String(32), nullable=False)
    index = db.Column(db.Integer, nullable=False)
    reached = db.Column(db.Boolean, nullable=False,default=False)

    reached_time = db.Column(db.DateTime, nullable=True)   
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   
