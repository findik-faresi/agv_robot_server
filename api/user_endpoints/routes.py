# api/user_bp/user_bp.py
from base.base_view import BaseView
from models.user import User  
from flask import Blueprint
from models.user import User
from base.base_view import BaseView

user_bp = Blueprint("user_bp", __name__)

class UserView(BaseView):
    model = User

user_view = UserView()

user_bp.add_url_rule("/user/", defaults={"id": None}, view_func=user_view.get, methods=["GET"])
user_bp.add_url_rule("/user/", view_func=user_view.post, methods=["POST"])
user_bp.add_url_rule("/user/<int:id>", view_func=user_view.get, methods=["GET"])
user_bp.add_url_rule("/user/<int:id>", view_func=user_view.put, methods=["PUT"])
user_bp.add_url_rule("/user/<int:id>", view_func=user_view.delete, methods=["DELETE"])
