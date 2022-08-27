from flask import request
from flask_restful import Resource

from managers.authentication import auth
from managers.videos import VideosManager
from schemas.response.videos import VideosSchemaResponse


class VideosResource(Resource):
    def get(self):
        videos = VideosManager.get_videos()
        return VideosSchemaResponse().dump(videos, many=True)


    #TODO must be moderator/admin to add videos
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        new_video = VideosManager.create(data, current_user)