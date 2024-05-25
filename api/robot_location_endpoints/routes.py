# api/robot_location_bp/robot_location_bp.py
from base.base_view import BaseView
from models.robot_location import RobotLocation  
from flask import Blueprint
from models.robot_location import RobotLocation 
from base.base_view import BaseView

robot_location_bp = Blueprint("robot_location_bp", __name__)

class RobotLocationView(BaseView):
    model = RobotLocation

robot_location_view = RobotLocationView()

robot_location_bp.add_url_rule("/robot_location/", defaults={"id": None}, view_func=robot_location_view.get, methods=["GET"])
robot_location_bp.add_url_rule("/robot_location/", view_func=robot_location_view.post, methods=["POST"])
robot_location_bp.add_url_rule("/robot_location/<int:id>", view_func=robot_location_view.get, methods=["GET"])
robot_location_bp.add_url_rule("/robot_location/<int:id>", view_func=robot_location_view.put, methods=["PUT"])
robot_location_bp.add_url_rule("/robot_location/<int:id>", view_func=robot_location_view.delete, methods=["DELETE"])
