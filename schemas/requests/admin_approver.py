from marshmallow import Schema, fields


class AdminPromotionSchema(Schema):
    email = fields.Email(required=True)


class AdminDemotionSchema(Schema):
    email = fields.Email(required=True)