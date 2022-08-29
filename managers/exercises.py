from database import db
from models import ExerciseModel
from utilities.validators import check_id_exists


class ExerciseManager:
    @staticmethod
    def create(data, user, id):
        data["workout_pk"] = id
        workout = ExerciseModel(**data)
        db.session.add(workout)
        db.session.flush()
        return workout


    @staticmethod
    def get_exercises(user, id):
        return ExerciseModel.query.filter_by(workout_pk=id)

class ExactExerciseManager:
    @staticmethod
    def put(data, exercise_id):
        check_id_exists(ExerciseModel, exercise_id)
        ExerciseModel.query.filter_by(id=exercise_id).update({
            "name": data["name"],
            "weight": data["weight"],
            "series": data["series"],
            "reps": data["reps"]
        })

    @staticmethod
    def delete(exercise_id):
        target = ExerciseModel.query.filter_by(id=exercise_id).first()
        db.session.delete(target)
        db.session.flush()