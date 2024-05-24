from flask import request, jsonify

class BaseView:
    model = None

    def get(self, id=None):
        if id:
            instance = self.model.query.get(id)
            return jsonify(instance.to_dict())
        instances = self.model.query.all()
        return jsonify([instance.to_dict() for instance in instances])

    def post(self):
        data = request.get_json()
        instance = self.model(**data)
        instance.save()
        return jsonify(instance.to_dict()), 201

    def put(self, id):
        data = request.get_json()
        instance = self.model.query.get(id)
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return jsonify(instance.to_dict())

    def delete(self, id):
        instance = self.model.query.get(id)
        instance.delete()
        return "[+] Data was successfully deleted.", 204

