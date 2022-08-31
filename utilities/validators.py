from marshmallow import ValidationError
from password_strength import PasswordPolicy
from werkzeug.exceptions import BadRequest

from models import RegularUser, UserRole, ModeratorUser, AdminUser

policy = PasswordPolicy.from_names(
    uppercase=1,  # ABCD
    numbers=1,  # 123456
    special=1,  # !@$%^.
)


def validate_password(password):
    password_errors = policy.test(password)
    if password_errors:
        raise ValidationError(
            "Password must contain one Uppercase, one Number and one Special character."
        )


def check_if_id_exists(model, id):
    target = model.query.filter_by(id=id).first()
    if not target:
        raise BadRequest("No such item!")


def model_checker_by_user_role(user, photo_url):
    role = user.role
    if role == UserRole.regular:
        return RegularUser.query.filter_by(pk=user.pk).update(
            {
                "photo_url": photo_url,
            }
        )
    elif role == UserRole.moderator:
        return ModeratorUser.query.filter_by(pk=user.pk).update(
            {
                "photo_url": photo_url,
            }
        )
    return AdminUser.query.filter_by(pk=user.pk).update(
        {
            "photo_url": photo_url,
        }
    )


def check_if_object_id_is_owned_by_user(user, id, table):
    object = table.query.filter_by(id=id).first()
    if not object.users_pk == user.pk:
        raise BadRequest("You don't have registered such item!")
