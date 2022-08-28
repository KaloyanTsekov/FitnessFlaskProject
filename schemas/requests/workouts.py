from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models import BodySection, DaysFromTheWeekend


class WorkoutSchemaRequest(Schema):
    name = fields.Str(required=True)
    category = EnumField(BodySection, required=True)
    day = EnumField(DaysFromTheWeekend, required=True)

