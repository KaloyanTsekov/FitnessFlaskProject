from database import db
from models import WorkoutModel
from utilities.validators import check_if_id_exists, check_if_object_id_is_owned_by_user


class WorkoutManager:
    @staticmethod
    def create(data, user):
        data["users_pk"] = user.pk
        workout = WorkoutModel(**data)
        db.session.add(workout)
        db.session.flush()
        return workout

    @staticmethod
    def get_workouts(user):
        return WorkoutModel.query.filter_by(users_pk=user.pk)


class ExactWorkoutManager:
    @staticmethod
    def put(user, workout_id, workout_model, data):
        check_if_id_exists(WorkoutModel, workout_id)
        check_if_object_id_is_owned_by_user(user, workout_id, workout_model)
        WorkoutModel.query.filter_by(id=workout_id).update({
            "name": data["name"],
            "category": data["category"],
            "day": data["day"]
        })

    @staticmethod
    def delete(user, workout_id, workout_model):
        check_if_id_exists(WorkoutModel, workout_id)
        check_if_object_id_is_owned_by_user(user, workout_id, workout_model)
        target = WorkoutModel.query.filter_by(id=workout_id).first()
        db.session.delete(target)
        db.session.flush()



