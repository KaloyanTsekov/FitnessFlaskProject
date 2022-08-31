from flask import request
from flask_api import status
from flask_restful import Resource

from managers.authentication import auth
from managers.videos import VideosManager, ExactVideoManager
from models import UserRole
from schemas.requests.videos import VideosSchemaRequest
from schemas.response.videos import VideosSchemaResponse
from utilities.decorators import permission_required, validate_schema


class VideosResource(Resource):
    @staticmethod
    def get():
        videos = VideosManager.get_videos()
        return VideosSchemaResponse().dump(videos, many=True)

    @auth.login_required
    @permission_required(UserRole.moderator)
    @validate_schema(VideosSchemaRequest)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        VideosManager.create(data, current_user)
        return {"Status": "Video created"}, status.HTTP_201_CREATED
        # return VideosSchemaResponse().dump(new_video), status.HTTP_201_CREATED   # AttributeError: 'str' object has no attribute 'name'


class ExactVideoResource(Resource):
    @auth.login_required
    @permission_required(UserRole.moderator)
    @validate_schema(VideosSchemaRequest)
    def put(self, id):
        data = request.get_json()
        auth.current_user()
        ExactVideoManager.put(data, id)
        return {"Status": "EDITED"}, status.HTTP_200_OK

    @auth.login_required
    @permission_required(UserRole.moderator)
    def delete(self, id):
        auth.current_user()
        ExactVideoManager.delete(id)
        return status.HTTP_204_NO_CONTENT
