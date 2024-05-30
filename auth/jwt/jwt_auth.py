from flask_jwt_extended import get_jwt_identity

class Auth:
    @staticmethod
    def jwt_authenticate():
        identity = get_jwt_identity()
        if not identity:
            return False
        return True
