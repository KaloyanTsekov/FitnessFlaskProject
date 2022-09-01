import os
import uuid

from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from database import db
from managers.authentication import AuthenticationManager
from models import RegularUser, ModeratorUser, AdminUser
from services.aws_s3 import S3Service
from services.aws_ses import SESService
from utilities.common import decode_file
from utilities.constants import TEMP_DIR, S3LINK
from utilities.validators import model_checker_by_user_role


def register_user(user_data, table):
    user_data["password"] = generate_password_hash(user_data["password"])
    user = table(**user_data)
    db.session.add(user)
    return AuthenticationManager.encode_token(user)


def login_user(login_data, table):
    user = table.query.filter_by(email=login_data["email"]).first()
    if not user:
        raise BadRequest("No such email! Please register!")
    if check_password_hash(user.password, login_data["password"]):
        return AuthenticationManager.encode_token(user)
    raise BadRequest("Wrong credentials!")


def delete_current_photo(user):
    photo_url = user.photo_url
    if len(photo_url) > 5:
        file_name = photo_url.split(S3LINK)[1]
        s3 = S3Service()
        s3.delete_photo(file_name)
        user.photo_url = "None"


class RegularUserManager:
    @staticmethod
    def register(regular_user_data):
        return register_user(regular_user_data, RegularUser)

    @staticmethod
    def login(login_data):
        # noinspection PyTypeChecker
        return login_user(login_data, RegularUser)


class ModeratorUserManager:
    @staticmethod
    def register(moderator_user_data):
        ses = SESService()
        ses.send_email(moderator_user_data["email"])
        return register_user(moderator_user_data, ModeratorUser)

    @staticmethod
    def login(login_data):
        # noinspection PyTypeChecker
        return login_user(login_data, ModeratorUser)


class AdminUserManager:
    @staticmethod
    def login(login_data):
        # noinspection PyTypeChecker
        return login_user(login_data, AdminUser)


class UserPhotoManager:
    @staticmethod
    def update(data, user):
        extension = data.pop("extension")
        photo = data.pop("encoded_photo")
        file_name = f"{str(uuid.uuid4())}.{extension}"
        path = os.path.join(TEMP_DIR, file_name)
        try:
            decode_file(path, photo)
            s3 = S3Service()
            delete_current_photo(user)
            photo_url = s3.upload_photo(path, file_name)
            model_checker_by_user_role(user, photo_url)
        finally:
            os.remove(path)

    @staticmethod
    def delete(user):
        delete_current_photo(user)
