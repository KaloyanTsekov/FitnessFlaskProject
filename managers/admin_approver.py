from werkzeug.exceptions import BadRequest

from models import ModeratorUser, UserRole


def change_moderator_status(email, role):
    moderator = ModeratorUser.query.filter_by(email=email).first()
    if not moderator:
        raise BadRequest("Moderator does not exist!")
    ModeratorUser.query.filter_by(email=email).update({"role": role})


class AdminApproverManager:
    @staticmethod
    def promote(email):
        return change_moderator_status(email, UserRole.moderator)


    @staticmethod
    def demote(email):
        return change_moderator_status(email, UserRole.regular)

