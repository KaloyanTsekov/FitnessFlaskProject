from flask import request
from flask_api import status
from flask_restful import Resource

from managers.admin_approver import AdminApproverManager
from managers.authentication import auth
from models import UserRole
from schemas.requests.admin_approver import AdminPromotionSchema, AdminDemotionSchema
from utilities.decorators import validate_schema, permission_required


class AdminPromotionResource(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(AdminPromotionSchema)
    def put(self):
        data = request.get_json()
        email = data["email"]
        auth.current_user()
        AdminApproverManager.promote(email)
        return {"Status": "Promoted"}, status.HTTP_200_OK


class AdminDemotionResource(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(AdminDemotionSchema)
    def put(self):
        data = request.get_json()
        email = data["email"]
        auth.current_user()
        AdminApproverManager.demote(email)
        return {"Status": "Demoted"}, status.HTTP_200_OK
