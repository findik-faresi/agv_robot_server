# api/connected_user_endpoints/connected_user_endpoints.py
from base.base_view import BaseView
from models.connected_user import ConnectedUser  
from flask import Blueprint

connected_user_bp = Blueprint("connected_user_bp", __name__)

class ConnectedUserView(BaseView):
    model = ConnectedUser

connected_user_view = ConnectedUserView()

connected_user_bp.add_url_rule("/connected_user/", defaults={"id": None}, view_func=connected_user_view.get, methods=["GET"])
connected_user_bp.add_url_rule("/connected_user/", view_func=connected_user_view.post, methods=["POST"])
connected_user_bp.add_url_rule("/connected_user/<int:id>", view_func=connected_user_view.get, methods=["GET"])
connected_user_bp.add_url_rule("/connected_user/<int:id>", view_func=connected_user_view.put, methods=["PUT"])
connected_user_bp.add_url_rule("/connected_user/<int:id>", view_func=connected_user_view.delete, methods=["DELETE"])
