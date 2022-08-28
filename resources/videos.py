from flask import request
from flask_api import status
from flask_restful import Resource

from managers.authentication import auth
from managers.videos import VideosManager
from models import UserRole
from schemas.response.videos import VideosSchemaResponse
from utilities.decorators import permission_required, validate_schema


class VideosResource(Resource):
    @staticmethod
    def get():
        videos = VideosManager.get_videos()
        return VideosSchemaResponse().dump(videos, many=True)

    @auth.login_required
    @permission_required(UserRole.regular)  #TODO must be moderator/admin to add videos
    @validate_schema(VideosSchemaResponse)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        new_video = VideosManager.create(data, current_user)
        return {"Status": "Video created"}, status.HTTP_201_CREATED
        #return VideosSchemaResponse().dump(new_video), status.HTTP_201_CREATED   # AttributeError: 'str' object has no attribute 'name'

    @auth.login_required
    @permission_required(UserRole.regular)  #TODO must be moderator/admin to add videos
    def put(self):
        pass

    @auth.login_required
    @permission_required(UserRole.regular)  #TODO must be moderator/admin to add videos
    def delete(self, id):
        current_user = auth.current_user()
        VideosManager.delete(id)
        return status.HTTP_204_NO_CONTENT