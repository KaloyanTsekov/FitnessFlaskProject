from flask_api import status

from database import db
from models import VideoModel


class VideosManager:
    @staticmethod
    def get_videos():
        return VideoModel.query.all()

    @staticmethod
    def create(data, user):
        data["users_pk"] = user.pk
        video = VideoModel(**data)
        db.session.add(video)
        db.session.flush()
        return video

    @staticmethod
    def delete(video_id):
        target = VideoModel.query.filter_by(id=video_id).first()
        db.session.delete(target)
        db.session.flush()


