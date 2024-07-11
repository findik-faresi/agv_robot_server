from models import User ,Robot, QRCode
from werkzeug.security import generate_password_hash
from helper import read_json
from . import DEFAULT_QR

def _init_admin(db):

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

def init_default_qr(db):
    robot = Robot.query.filter(Robot.id > 0).first()

    for qr in DEFAULT_QR:
        if not QRCode.query.filter_by(area_name=qr.get("area_name")).first():
            db.session.add(QRCode(
                robot_id = robot.id,
                vertical_coordinate = qr.get("vertical_coordinate"),
                horizontal_coordinate = qr.get("horizontal_coordinate"),
                area_name = qr.get("area_name")
            ))

    db.session.commit()
