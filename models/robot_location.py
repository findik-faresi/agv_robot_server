from database.database import db
from datetime import datetime 

class RobotLocation(db.Model):
    __tablename__ = "robot_location"

    id = db.Column(db.Integer, primary_key=True)
    
    mission_id = db.Column(db.Integer, db.ForeignKey("mission.id"), nullable=False)
    distance_traveled = db.Column(db.Float,nullable=False)
    traveled_direction = db.Column(db.Integer,nullable=False)

    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)   

