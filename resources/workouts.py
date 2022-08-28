from flask import request
from flask_api import status
from flask_restful import Resource

from managers.authentication import auth
from managers.workouts import WorkoutManager, ExactWorkoutManager
from models import UserRole
from schemas.requests.workouts import WorkoutSchemaRequest
from schemas.response.workouts import WorkoutSchemaResponse
from utilities.decorators import permission_required, validate_schema


class WorkoutResource(Resource):
    @auth.login_required
    @permission_required(UserRole.regular)
    @validate_schema(WorkoutSchemaRequest)
    def post(self):
        data = request.get_json()
        user = auth.current_user()
        WorkoutManager.create(data, user)
        return {"Status": "Workout created"}, status.HTTP_201_CREATED

    @auth.login_required
    @permission_required(UserRole.regular)
    def get(self):
        user = auth.current_user()
        workouts = WorkoutManager.get_videos(user)
        return WorkoutSchemaResponse().dump(workouts, many=True)


class ExactWorkoutResource(Resource):
    @auth.login_required
    @permission_required(UserRole.regular)
    @validate_schema(WorkoutSchemaRequest)
    def put(self, id):
        data = request.get_json()
        auth.current_user()
        ExactWorkoutManager.put(data, id)
        return {"Status": "EDITED"}, status.HTTP_200_OK

    @auth.login_required
    @permission_required(UserRole.regular)
    def delete(self, id):
        auth.current_user()
        ExactWorkoutManager.delete(id)
        return status.HTTP_204_NO_CONTENT