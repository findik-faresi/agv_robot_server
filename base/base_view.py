from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

class BaseView:
    model = None

    @staticmethod
    def jwt_authenticate():
        identity = get_jwt_identity()
        if not identity:
            return False
        return True

    @jwt_required()
    def get(self, id=None):
        if not self.jwt_authenticate():
            return jsonify({"message": "Unauthorized"}), 401

        if id:
            instance = self.model.query.get(id)
            return jsonify(instance.to_dict())
        instances = self.model.query.all()
        return jsonify([instance.to_dict() for instance in instances])

    @jwt_required()
    def post(self):
        if not self.jwt_authenticate():
            return jsonify({"message": "Unauthorized"}), 401

        data = request.get_json()
        instance = self.model(**data)
        instance.save()
        return jsonify(instance.to_dict()), 201

    @jwt_required()
    def put(self, id):
        if not self.jwt_authenticate():
            return jsonify({"message": "Unauthorized"}), 401

        data = request.get_json()
        instance = self.model.query.get(id)
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return jsonify(instance.to_dict())

    @jwt_required()
    def delete(self, id):
        if not self.jwt_authenticate():
            return jsonify({"message": "Unauthorized"}), 401

        instance = self.model.query.get(id)
        instance.delete()
        return "[+] Data was successfully deleted.", 204

