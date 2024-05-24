# api/user_endpoints/__init__.py

from flask import Blueprint
from models.user import User
from base.base_view import BaseView

user_endpoints = Blueprint("user_endpoints", __name__)

from .user_endpoints import user_endpoints

