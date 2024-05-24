# api/user_endpoints/user_endpoints.py
from . import user_endpoints
from base.base_view import BaseView
from models.user import User  

class UserView(BaseView):
    model = User

user_view = UserView()

user_endpoints.add_url_rule('/users/', defaults={'id': None}, view_func=user_view.get, methods=['GET'])
user_endpoints.add_url_rule('/users/', view_func=user_view.post, methods=['POST'])
user_endpoints.add_url_rule('/users/<int:id>', view_func=user_view.get, methods=['GET'])
user_endpoints.add_url_rule('/users/<int:id>', view_func=user_view.put, methods=['PUT'])
user_endpoints.add_url_rule('/users/<int:id>', view_func=user_view.delete, methods=['DELETE'])

