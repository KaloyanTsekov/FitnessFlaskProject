from datetime import datetime, timedelta
import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import Unauthorized

from models import RegularUser


class AuthenticationManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.pk, "exp": datetime.utcnow() + timedelta(days=1)}
        return jwt.encode(payload, key=config("JWT_SECRET"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        if not token:
            raise Unauthorized("Missing token")
        try:
            payload = jwt.decode(token, key=config("JWT_SECRET"), algorithms=["HS256"])
            return payload["sub"]
        except ExpiredSignatureError:
            raise Unauthorized("Token expired")
        except InvalidTokenError:
            raise Unauthorized("Invalid token")


auth = HTTPTokenAuth()


@auth.verify_token
def verify(token):
    user_id = AuthenticationManager.decode_token(token)
    print(RegularUser.query.filter_by(pk=user_id).first())

    return RegularUser.query.filter_by(pk=user_id).first()