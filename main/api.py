from flask import jsonify
from . import main_bp
from database.database import db 
import models 

@main_bp.route("/room")
def room():
    rooms = Room.query.all()
    response_data = [
        {
            "id": room.id,
            "room_name": room.room_name, 
            "is_active": room.is_active,
            "created_date":room.created_date
        } for room in rooms] 
    return jsonify(response_data)

@main_bp.route("/connected_user_info")
def connected_user_info():
    connected_users = ConnectedUserInfo.query.all()
    response_data = [
        {
             
        } for connected_user in connected_users] 
    return jsonify(response_data)
