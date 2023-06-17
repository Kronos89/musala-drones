from app import db

class Drone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(100), unique=True, nullable=False)
    model = db.Column(db.String(50), nullable=False)
    weight_limit = db.Column(db.Float, nullable=False)
    battery_capacity = db.Column(db.Float, nullable=False)
    state = db.Column(db.String(50), nullable=False)

    #Medication table
    medications = db.relationship('Medication', backref='drone', lazy=True)
