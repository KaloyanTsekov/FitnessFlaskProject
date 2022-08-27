from flask_restful import Resource
from flask import request
from flask_api import status

from managers.users import RegularUserManager


class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        token = RegularUserManager.register(data)
        return {"token": token}, status.HTTP_201_CREATED
