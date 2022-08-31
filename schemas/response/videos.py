from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models import BodySection


class VideosSchemaResponse(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    category = EnumField(BodySection, required=True)
    youtube_link = fields.Str(required=True)
    users_pk = fields.Int(required=True)
