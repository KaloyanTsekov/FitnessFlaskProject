from flask import request
from flask_api import status
from flask_restful import Resource

from managers.authentication import auth
from managers.users import UserPhotoManager
from schemas.requests.users import ChangePhotoSchemaRequest
from utilities.decorators import validate_schema


class UserPhotoResource(Resource):
    @auth.login_required
    @validate_schema(ChangePhotoSchemaRequest)
    def put(
        self,
    ):
        data = request.get_json()
        user = auth.current_user()
        UserPhotoManager.update(data, user)
        return {"Status": "Photo has been changed"}, status.HTTP_200_OK

    @auth.login_required
    def delete(
        self,
    ):
        user = auth.current_user()
        UserPhotoManager.delete(user)
        return status.HTTP_204_NO_CONTENT
