from flask import Flask
from database.database import init_db,db
from flask_migrate import Migrate
import secrets
from flask_jwt_extended import JWTManager
from datetime import timedelta

from api import * 
from auth.login import login_bp

from network import socketio 

from network.join_robot import join_robot 
from network.join_user import join_user 

from network.leave_robot import leave_robot 
from network.leave_user import leave_user 

from network.disconnect import disconnect 

from network.camera import camera
from network.location import location 
from network.mission import mission 
from network.qr_code import qr_code 
from network.road_map import road_map 
from network.status import status 

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(16) 
secret_key = secrets.token_urlsafe(32)
app.config["JWT_SECRET_KEY"] = secret_key
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=4)
jwt = JWTManager(app)

init_db(app)

migrate = Migrate(app,db)

app.register_blueprint(connected_robot_bp,url_prefix="/api")
app.register_blueprint(connected_user_bp,url_prefix="/api")
app.register_blueprint(mission_bp,url_prefix="/api")
app.register_blueprint(qr_code_bp,url_prefix="/api")
app.register_blueprint(road_map_bp,url_prefix="/api")
app.register_blueprint(robot_bp,url_prefix="/api")
app.register_blueprint(robot_location_bp,url_prefix="/api")
app.register_blueprint(room_bp,url_prefix="/api")
app.register_blueprint(user_bp,url_prefix="/api")
app.register_blueprint(login_bp,url_prefix="/auth")

socketio.init_app(app)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
