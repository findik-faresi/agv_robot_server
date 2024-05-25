from flask import Flask
from flask_socketio import SocketIO
from network import socketio as main_socketio
from secrets import token_hex
from database.database import init_db,db
from flask_migrate import Migrate
import models 
from api import * 

app = Flask(__name__)
app.config["SECRET_KEY"] = token_hex(16) 

init_db(app)
migrate = Migrate(app,db)

app.register_blueprint(connected_robot_info_bp,url_prefix="/api")
app.register_blueprint(connected_user_info_bp,url_prefix="/api")
app.register_blueprint(mission_bp,url_prefix="/api")
app.register_blueprint(qr_code_data_bp,url_prefix="/api")
app.register_blueprint(road_map_bp,url_prefix="/api")
app.register_blueprint(robot_bp,url_prefix="/api")
app.register_blueprint(robot_location_bp,url_prefix="/api")
app.register_blueprint(room_bp,url_prefix="/api")
app.register_blueprint(turn_point_bp,url_prefix="/api")
app.register_blueprint(user_bp,url_prefix="/api")

socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
