# api/qr_code_data_endpoints/qr_code_data_endpoints.py
from base.base_view import BaseView
from models.qr_code_data import QRCodeData  
from flask import Blueprint

qr_code_data_bp = Blueprint("qr_code_data_bp", __name__)

class QRCodeDataView(BaseView):
    model = QRCodeData

qr_code_data_view = QRCodeDataView()

qr_code_data_bp.add_url_rule("/qr_code_data/", defaults={"id": None}, view_func=qr_code_data_view.get, methods=["GET"])
qr_code_data_bp.add_url_rule("/qr_code_data/", view_func=qr_code_data_view.post, methods=["POST"])
qr_code_data_bp.add_url_rule("/qr_code_data/<int:id>", view_func=qr_code_data_view.get, methods=["GET"])
qr_code_data_bp.add_url_rule("/qr_code_data/<int:id>", view_func=qr_code_data_view.put, methods=["PUT"])
qr_code_data_bp.add_url_rule("/qr_code_data/<int:id>", view_func=qr_code_data_view.delete, methods=["DELETE"])
