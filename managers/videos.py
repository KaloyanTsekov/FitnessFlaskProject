from models import VideoModel


class VideosManager:
    @staticmethod
    def get_videos():
        return VideoModel.query.all()