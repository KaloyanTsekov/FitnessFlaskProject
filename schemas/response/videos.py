from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models import VideoModel


class VideosSchemaResponse(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    category = EnumField(VideoModel, by_value=True)
    youtube_link = fields.Str(required=True)
