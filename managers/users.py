from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

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

    @staticmethod
    def login(login_data):
        regular_user = RegularUser.query.filter_by(email=login_data["email"]).first()
        if not regular_user:
            raise BadRequest("No such email! Please register!")
        if check_password_hash(regular_user.password, login_data["password"]):
            return AuthenticationManager.encode_token(regular_user),
        raise BadRequest("Wrong credentials!")