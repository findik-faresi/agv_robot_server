# api/turn_point_bp/turn_point_bp.py
from base.base_view import BaseView
from models.turn_point import TurnPoint  
from flask import Blueprint

turn_point_bp = Blueprint("turn_point_bp", __name__)

class TurnPointView(BaseView):
    model = TurnPoint

turn_point_view = TurnPointView()

turn_point_bp.add_url_rule("/turn_point/", defaults={"id": None}, view_func=turn_point_view.get, methods=["GET"])
turn_point_bp.add_url_rule("/turn_point/", view_func=turn_point_view.post, methods=["POST"])
turn_point_bp.add_url_rule("/turn_point/<int:id>", view_func=turn_point_view.get, methods=["GET"])
turn_point_bp.add_url_rule("/turn_point/<int:id>", view_func=turn_point_view.put, methods=["PUT"])
turn_point_bp.add_url_rule("/turn_point/<int:id>", view_func=turn_point_view.delete, methods=["DELETE"])
