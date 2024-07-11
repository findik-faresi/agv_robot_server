# authentication/login.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from models import User,Robot
from termcolor import colored

login_bp = Blueprint("login_bp", __name__)

@login_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid username or password"}), 401

    print(colored(f"[+] {username} login :)", "green"))
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@login_bp.route("/_login", methods=["POST"])
def robot_login():
    data = request.json
    serial_number = data.get("serial_number")
    secret_key = data.get("secret_key")

    if not serial_number or not secret_key:
        return jsonify({"message": "Serial number and secret key are required"}), 400

    robot = Robot.query.filter_by(serial_number=serial_number).first()
    if not robot or not check_password_hash(robot.secret_key, secret_key):
        return jsonify({"message": "Invalid serial number or secret key"}), 401

    print(colored(f"[+] {serial_number} login :)", "green"))
    access_token = create_access_token(identity=serial_number)
    return jsonify(access_token=access_token), 200
