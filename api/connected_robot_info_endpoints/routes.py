# api/connected_robot_info_endpoints/connected_robot_info_endpoints.py
from base.base_view import BaseView
from models.connected_robot_info import ConnectedRobotInfo  
from flask import Blueprint

connected_robot_info_bp = Blueprint("connected_robot_info_bp", __name__)

class ConnectedRobotInfoView(BaseView):
    model = ConnectedRobotInfo

connected_robot_info_view = ConnectedRobotInfoView()

connected_robot_info_bp.add_url_rule("/connected_robot_info/", defaults={"id": None}, view_func=connected_robot_info_view.get, methods=["GET"])
connected_robot_info_bp.add_url_rule("/connected_robot_info/", view_func=connected_robot_info_view.post, methods=["POST"])
connected_robot_info_bp.add_url_rule("/connected_robot_info/<int:id>", view_func=connected_robot_info_view.get, methods=["GET"])
connected_robot_info_bp.add_url_rule("/connected_robot_info/<int:id>", view_func=connected_robot_info_view.put, methods=["PUT"])
