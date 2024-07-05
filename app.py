from flask import Flask
from secrets import token_hex
from database.database import init_db,db
from flask_migrate import Migrate
import secrets
from flask_jwt_extended import JWTManager

from api import * 
from auth.login import login_bp

from network import socketio 

from network.join import user,robot
from network.leave import user,robot

from network.disconnect.disconnect import handle_disconnect

from network.location.controller import _c0
from network.mission.controller import _c1 
from network.qr_code.controller import _c2
from network.status.controller import _c3
from network.road_map.controller import _c5
from network.camera.controller import _c6

from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = token_hex(16) 
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
