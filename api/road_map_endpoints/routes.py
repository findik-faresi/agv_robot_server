# api/road_map_bp/road_map_bp.py
from base.base_view import BaseView
from models.road_map import RoadMap  
from flask import Blueprint

road_map_bp = Blueprint("road_map_bp", __name__)

class RoadMapView(BaseView):
    model = RoadMap

road_map_view = RoadMapView()

road_map_bp.add_url_rule("/road_map/", defaults={"id": None}, view_func=road_map_view.get, methods=["GET"])
road_map_bp.add_url_rule("/road_map/", view_func=road_map_view.post, methods=["POST"])
road_map_bp.add_url_rule("/road_map/<int:id>", view_func=road_map_view.get, methods=["GET"])
road_map_bp.add_url_rule("/road_map/<int:id>", view_func=road_map_view.put, methods=["PUT"])
road_map_bp.add_url_rule("/road_map/<int:id>", view_func=road_map_view.delete, methods=["DELETE"])
