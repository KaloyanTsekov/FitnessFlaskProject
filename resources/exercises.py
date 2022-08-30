from flask import request
from flask_api import status
from flask_restful import Resource

from managers.authentication import auth
from managers.exercises import ExerciseManager, ExactExerciseManager
from models import UserRole
from schemas.requests.exercises import ExerciseSchemaRequest
from schemas.response.exercises import ExerciseSchemaResponse
from utilities.decorators import permission_required, validate_schema


class ExerciseResource(Resource):
    @auth.login_required
    @permission_required(UserRole.regular)
    @validate_schema(ExerciseSchemaRequest)
    def post(self, id):
        data = request.get_json()
        user = auth.current_user()
        ExerciseManager.create(data, user, id)
        return {"Status": "Exercise created"}, status.HTTP_201_CREATED

    @auth.login_required
    @permission_required(UserRole.regular)
    def get(self, id):
        user = auth.current_user()
        workouts = ExerciseManager.get_exercises(user, id)
        return ExerciseSchemaResponse().dump(workouts, many=True)


class ExactExerciseResource(Resource):
    @auth.login_required
    @permission_required(UserRole.regular)
    @validate_schema(ExerciseSchemaRequest)
    def put(self, id):
        data = request.get_json()
        user = auth.current_user()
        ExactExerciseManager.put(data, id, user)
        return {"Status": "EDITED"}, status.HTTP_200_OK

    @auth.login_required
    @permission_required(UserRole.regular)
    def delete(self, id):
        user = auth.current_user()
        ExactExerciseManager.delete(user, id)
        return status.HTTP_204_NO_CONTENT