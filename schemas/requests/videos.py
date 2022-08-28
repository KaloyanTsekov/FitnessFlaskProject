from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models import BodySection


class VideosSchemaRequest(Schema):
    name = fields.Str(required=True)
    category = EnumField(BodySection, required=True)
    youtube_link = fields.Str(required=True)
