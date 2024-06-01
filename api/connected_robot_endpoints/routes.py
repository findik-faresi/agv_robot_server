# api/connected_robot_endpoints/connected_robot_endpoints.py
from base.base_view import BaseView
from models.connected_robot import ConnectedRobot  
from flask import Blueprint

connected_robot_bp = Blueprint("connected_robot_bp", __name__)

class ConnectedRobotView(BaseView):
    model = ConnectedRobot

connected_robot_view = ConnectedRobotView()

connected_robot_bp.add_url_rule("/connected_robot/", defaults={"id": None}, view_func=connected_robot_view.get, methods=["GET"])
connected_robot_bp.add_url_rule("/connected_robot/", view_func=connected_robot_view.post, methods=["POST"])
connected_robot_bp.add_url_rule("/connected_robot/<int:id>", view_func=connected_robot_view.get, methods=["GET"])
connected_robot_bp.add_url_rule("/connected_robot/<int:id>", view_func=connected_robot_view.put, methods=["PUT"])
