from database import db
from models import VideoModel


class VideosManager:
    @staticmethod
    def get_videos():
        return VideoModel.query.all()

    #TODO must be moderator/admin to add videos
    @staticmethod
    def create(data, user):
        video = VideoModel(**data)
        db.session.add(video)
        db.session.flush()
        return video
