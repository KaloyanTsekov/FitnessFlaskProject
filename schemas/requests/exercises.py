from marshmallow import Schema, fields


class ExerciseSchemaRequest(Schema):
    name = fields.Str(required=True)
    weight = fields.Float(required=True)
    series = fields.Int(required=True)
    reps = fields.Int(required=True)
