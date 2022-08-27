from marshmallow import ValidationError
from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(
    uppercase=1,   # ABCD
    numbers=1,     # 123456
    special=1,     # !@$%^.
)


def validate_password(password):
    password_errors = policy.test(password)
    if password_errors:
        raise ValidationError("Password must contain one Uppercase, one Number and one Special character.")

