from flask_restful import Resource

from managers.videos import VideosManager
from schemas.response.videos import VideosSchemaResponse


class VideosResource(Resource):
    def get(self):
        videos = VideosManager.get_videos()
        return VideosSchemaResponse().dump(videos, many=True)