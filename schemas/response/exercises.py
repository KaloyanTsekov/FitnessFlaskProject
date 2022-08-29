from marshmallow import Schema, fields


class ExerciseSchemaResponse(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    weight = fields.Float(required=True)
    series = fields.Int(required=True)
    reps = fields.Int(required=True)
    workout_pk = fields.Int(required=True)