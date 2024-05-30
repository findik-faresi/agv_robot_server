# api/robot_bp/robot_bp.py
from base.base_view import BaseView
from models.robot import Robot  
from flask import Blueprint

robot_bp = Blueprint("robot_endpoint", __name__)

class RobotView(BaseView):
    model = Robot

robot_view = RobotView()

robot_bp.add_url_rule("/robot/", defaults={"id": None}, view_func=robot_view.get, methods=["GET"])
robot_bp.add_url_rule("/robot/", view_func=robot_view.post, methods=["POST"])
robot_bp.add_url_rule("/robot/<int:id>", view_func=robot_view.get, methods=["GET"])
robot_bp.add_url_rule("/robot/<int:id>", view_func=robot_view.put, methods=["PUT"])
robot_bp.add_url_rule("/robot/<int:id>", view_func=robot_view.delete, methods=["DELETE"])
