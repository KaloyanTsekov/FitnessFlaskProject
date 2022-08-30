from database import db
from models import VideoModel
from utilities.validators import check_if_id_exists


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


class ExactVideoManager:
    @staticmethod
    def put(data, video_id):
        check_if_id_exists(VideoModel, video_id)
        VideoModel.query.filter_by(id=video_id).update({
            "name": data["name"],
            "category": data["category"],
            "youtube_link": data["youtube_link"]
        })

    @staticmethod
    def delete(video_id):
        target = VideoModel.query.filter_by(id=video_id).first()
        db.session.delete(target)
        db.session.flush()


