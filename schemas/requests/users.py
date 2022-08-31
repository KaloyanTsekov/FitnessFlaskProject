from marshmallow import Schema, fields


class ChangePhotoSchemaRequest(Schema):
    extension = fields.Str(required=True)
    encoded_photo = fields.Str(required=True)
