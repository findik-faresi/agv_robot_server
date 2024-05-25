# api/room_bp/room_bp.py
from base.base_view import BaseView
from models.room import Room  
from flask import Blueprint
from models.room import Room 
from base.base_view import BaseView

room_bp = Blueprint("room_bp", __name__)

class RoomView(BaseView):
    model = Room

room_view = RoomView()

room_bp.add_url_rule("/room/", defaults={"id": None}, view_func=room_view.get, methods=["GET"])
room_bp.add_url_rule("/room/", view_func=room_view.post, methods=["POST"])
room_bp.add_url_rule("/room/<int:id>", view_func=room_view.get, methods=["GET"])
room_bp.add_url_rule("/room/<int:id>", view_func=room_view.put, methods=["PUT"])
room_bp.add_url_rule("/room/<int:id>", view_func=room_view.delete, methods=["DELETE"])
