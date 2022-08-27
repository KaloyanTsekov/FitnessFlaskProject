from werkzeug.security import generate_password_hash

from database import db
from managers.authentication import AuthenticationManager
from models import RegularUser


class RegularUserManager:
    @staticmethod
    def register(regular_user_data):
        regular_user_data["password"] = generate_password_hash(regular_user_data["password"])
        user = RegularUser(**regular_user_data)
        db.session.add(user)
        return AuthenticationManager.encode_token(user)