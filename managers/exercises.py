from database import db
from models import ExerciseModel, WorkoutModel
from utilities.validators import check_if_id_exists, check_if_object_id_is_owned_by_user


class ExerciseManager:
    @staticmethod
    def create(data, user, workout_id):
        check_if_id_exists(WorkoutModel, workout_id)
        check_if_object_id_is_owned_by_user(user, workout_id, WorkoutModel)
        data["workout_pk"] = workout_id
        workout = ExerciseModel(**data)
        db.session.add(workout)
        db.session.flush()
        return workout

    @staticmethod
    def get_exercises(user, id):
        return ExerciseModel.query.filter_by(workout_pk=id)


class ExactExerciseManager:
    @staticmethod
    def put(data, exercise_id, user):
        check_if_id_exists(ExerciseModel, exercise_id)
        current_exercise = ExerciseModel.query.filter_by(id=exercise_id).first()
        check_if_object_id_is_owned_by_user(
            user, current_exercise.workout_pk, WorkoutModel
        )
        ExerciseModel.query.filter_by(id=exercise_id).update(
            {
                "name": data["name"],
                "weight": data["weight"],
                "series": data["series"],
                "reps": data["reps"],
            }
        )

    @staticmethod
    def delete(user, exercise_id):
        check_if_id_exists(ExerciseModel, exercise_id)
        current_exercise = ExerciseModel.query.filter_by(id=exercise_id).first()
        check_if_object_id_is_owned_by_user(
            user, current_exercise.workout_pk, WorkoutModel
        )
        db.session.delete(current_exercise)
        db.session.flush()
