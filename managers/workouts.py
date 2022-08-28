from database import db
from models import WorkoutModel
from utilities.validators import check_id_exists


class WorkoutManager:
    @staticmethod
    def create(data, user):
        data["users_pk"] = user.pk
        workout = WorkoutModel(**data)
        db.session.add(workout)
        db.session.flush()
        return workout

    @staticmethod
    def get_videos(user):
        return WorkoutModel.query.filter_by(users_pk=user.pk)


class ExactWorkoutManager:
    @staticmethod
    def put(data, video_id):
        check_id_exists(WorkoutModel, video_id)
        WorkoutModel.query.filter_by(id=video_id).update({
            "name": data["name"],
            "category": data["category"],
            "day": data["day"]
        })

    @staticmethod
    def delete(video_id):
        target = WorkoutModel.query.filter_by(id=video_id).first()
        db.session.delete(target)
        db.session.flush()



