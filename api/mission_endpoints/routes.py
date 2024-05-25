# api/mission_endpoints/mission_endpoints.py
from base.base_view import BaseView
from models.mission import Mission  
from flask import Blueprint
from models.mission import Mission
from base.base_view import BaseView

mission_bp = Blueprint("mission_bp", __name__)

class MissionView(BaseView):
    model = Mission 

mission_view = MissionView()

mission_bp.add_url_rule("/mission/", defaults={"id": None}, view_func=mission_view.get, methods=["GET"])
mission_bp.add_url_rule("/mission/", view_func=mission_view.post, methods=["POST"])
mission_bp.add_url_rule("/mission/<int:id>", view_func=mission_view.get, methods=["GET"])
mission_bp.add_url_rule("/mission/<int:id>", view_func=mission_view.put, methods=["PUT"])
mission_bp.add_url_rule("/mission/<int:id>", view_func=mission_view.delete, methods=["DELETE"])
