# api/qr_code_endpoints/qr_code_endpoints.py
from base.base_view import BaseView
from models.qr_code import QRCode  
from flask import Blueprint

qr_code_bp = Blueprint("qr_code_bp", __name__)

class QRCodeView(BaseView):
    model = QRCode

qr_code_view = QRCodeView()

qr_code_bp.add_url_rule("/qr_code/", defaults={"id": None}, view_func=qr_code_view.get, methods=["GET"])
qr_code_bp.add_url_rule("/qr_code/", view_func=qr_code_view.post, methods=["POST"])
qr_code_bp.add_url_rule("/qr_code/<int:id>", view_func=qr_code_view.get, methods=["GET"])
qr_code_bp.add_url_rule("/qr_code/<int:id>", view_func=qr_code_view.put, methods=["PUT"])
qr_code_bp.add_url_rule("/qr_code/<int:id>", view_func=qr_code_view.delete, methods=["DELETE"])
