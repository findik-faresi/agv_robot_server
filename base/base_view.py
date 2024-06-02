from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from auth.jwt.jwt_auth import Auth

class BaseView:
    model = None

    @jwt_required()
    def get(self, id=None):
        try:
            if not Auth.jwt_authenticate():
                return jsonify({"message": "Unauthorized"}), 401

            if id:
                instance = self.model.query.get(id)
                if not instance:
                    return jsonify({"message": "Not Found"}), 404
                return jsonify(instance.to_dict())
            instances = self.model.query.all()
            return jsonify([instance.to_dict() for instance in instances])
        except Exception as e:
            return jsonify({"message": str(e)}), 500

    @jwt_required()
    def post(self):
        try:
            if not Auth.jwt_authenticate():
                return jsonify({"message": "Unauthorized"}), 401

            data = request.get_json()
            instance = self.model(**data)
            instance.save()
            return jsonify(instance.to_dict()), 201
        except Exception as e:
            return jsonify({"message": str(e)}), 500

    @jwt_required()
    def put(self, id):
        try:
            if not Auth.jwt_authenticate():
                return jsonify({"message": "Unauthorized"}), 401

            data = request.get_json()
            instance = self.model.query.get(id)
            if not instance:
                return jsonify({"message": "Not Found"}), 404
            for key, value in data.items():
                setattr(instance, key, value)
            instance.save()
            return jsonify(instance.to_dict())
        except Exception as e:
            return jsonify({"message": str(e)}), 500

    @jwt_required()
    def delete(self, id):
        try:
            if not Auth.jwt_authenticate():
                return jsonify({"message": "Unauthorized"}), 401

            instance = self.model.query.get(id)
            if not instance:
                return jsonify({"message": "Not Found"}), 404
            instance.delete()
            return jsonify({"message": "Data was successfully deleted."}), 204
        except Exception as e:
            return jsonify({"message": str(e)}), 500
