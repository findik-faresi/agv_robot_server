# api/connected_user_info_endpoints/connected_user_info_endpoints.py
from base.base_view import BaseView
from models.connected_user_info import ConnectedUserInfo  
from flask import Blueprint
from models.connected_user_info import ConnectedUserInfo 
from base.base_view import BaseView

connected_user_info_bp = Blueprint("connected_user_info_bp", __name__)

class ConnectedUserInfoView(BaseView):
    model = ConnectedUserInfo

connected_user_info_view = ConnectedUserInfoView()

connected_user_info_bp.add_url_rule("/connected_user_info/", defaults={"id": None}, view_func=connected_user_info_view.get, methods=["GET"])
connected_user_info_bp.add_url_rule("/connected_user_info/", view_func=connected_user_info_view.post, methods=["POST"])
connected_user_info_bp.add_url_rule("/connected_user_info/<int:id>", view_func=connected_user_info_view.get, methods=["GET"])
connected_user_info_bp.add_url_rule("/connected_user_info/<int:id>", view_func=connected_user_info_view.put, methods=["PUT"])
connected_user_info_bp.add_url_rule("/connected_user_info/<int:id>", view_func=connected_user_info_view.delete, methods=["DELETE"])
