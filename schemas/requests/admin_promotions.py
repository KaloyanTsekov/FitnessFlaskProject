from marshmallow import Schema, fields, validate

class AdminPromotionsSchema(Schema):
    email = fields.Email(required=True)