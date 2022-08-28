from flask_restful import Resource
from flask import request
from flask_api import status

from managers.users import RegularUserManager, ModeratorUserManager, AdminUserManager
from schemas.requests.authentication import LoginSchemaRequest, RegisterSchemaRequest
from utilities.decorators import validate_schema


class RegisterResource(Resource):
    @validate_schema(RegisterSchemaRequest)
    def post(self):
        data = request.get_json()
        token = RegularUserManager.register(data)
        return {"token": token}, status.HTTP_201_CREATED


class LoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = RegularUserManager.login(data)
        return {"token": token}, status.HTTP_200_OK


class ModeratorRegisterResource(Resource):
    @validate_schema(RegisterSchemaRequest)
    def post(self):
        data = request.get_json()
        token = ModeratorUserManager.register(data)
        return {"token": token}, status.HTTP_201_CREATED


class ModeratorLoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = ModeratorUserManager.login(data)
        return {"token": token}, status.HTTP_200_OK


class AdminLoginResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = AdminUserManager.login(data)
        return {"token": token}, status.HTTP_200_OK
