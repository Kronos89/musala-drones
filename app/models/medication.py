from app import db

class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.String(100), nullable=True)
    drone_id = db.Column(db.Integer, db.ForeignKey('drone.id'), nullable=True)
