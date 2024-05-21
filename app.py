from flask import Flask
from flask_socketio import SocketIO
from main import main_bp, socketio as main_socketio
from secrets import token_hex
from database.database import init_db,db
from flask_migrate import Migrate
import models 

app = Flask(__name__)
app.config["SECRET_KEY"] = token_hex(16) 

init_db(app)
migrate = Migrate(app,db)

app.register_blueprint(main_bp)

socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
