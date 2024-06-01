from models import User ,Robot
from werkzeug.security import generate_password_hash
from helper import read_json

def _init(db):

    data = read_json("./init/init.json")

    if not User.query.filter_by(username=data["admin"]["username"]).first():
        admin = User(
            username=data["admin"]["username"],
            password=generate_password_hash(data["admin"]["password"]),
            role=data["admin"]["role"]
        )
        db.session.add(admin)
    
    if not Robot.query.filter_by(serial_number=data["robot"]["serial_number"]).first():
        robot = Robot(
            serial_number=data["robot"]["serial_number"],
            secret_key=generate_password_hash(data["robot"]["secret_key"])
        )
        db.session.add(robot)

    db.session.commit()
