from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models import BodySection, DaysFromTheWeekend


class WorkoutSchemaResponse(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    category = EnumField(BodySection, required=True)
    day = EnumField(DaysFromTheWeekend, required=True)
    users_pk = fields.Int(required=True)
