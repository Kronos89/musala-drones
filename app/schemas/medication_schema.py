from marshmallow import Schema, fields, validate

class MedicationSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Regexp(r'^[\w-]+$',
                      error='Name can only contain letters, numbers, dashes, and underscores.'))
    weight = fields.Float(required=True)
    code = fields.Str(required=True, validate=validate.Regexp(r'^[A-Z0-9_]+$',
                      error='Code can only contain upper case letters, numbers and underscores.'))
    image = fields.Str(validate=validate.URL())
    drone_id = fields.Int()
