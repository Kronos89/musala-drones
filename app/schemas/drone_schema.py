from marshmallow import Schema, fields, validate

class DroneSchema(Schema):
    id = fields.Int(dump_only=True)
    serial_number = fields.Str(required=True, validate=validate.Length(max=100))
    model = fields.Str(required=True, validate=validate.OneOf(['Lightweight', 'Middleweight', 'Cruiserweight', 'Heavyweight']))
    weight_limit = fields.Float(required=True, validate=validate.Range(max=500))
    battery_capacity = fields.Float(required=True, validate=validate.Range(min=0, max=100))
    state = fields.Str(required=True, validate=validate.OneOf(['IDLE', 'LOADING', 'LOADED', 'DELIVERING', 'DELIVERED', 'RETURNING']))