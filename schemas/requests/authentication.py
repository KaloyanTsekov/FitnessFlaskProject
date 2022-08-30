from marshmallow import Schema, fields, validate
from marshmallow.validate import Length

from utilities.validators import validate_password


# noinspection PyTypeChecker
class RegisterSchemaRequest(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.And(validate_password, validate.Length(min=6, max=20)))
    #photo_url = fields.Str(required=True)

class LoginSchemaRequest(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
