from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app import db
from app.models.drone import Drone
from app.models.medication import Medication
from app.schemas.drone_schema import DroneSchema
from app.schemas.medication_schema import MedicationSchema

bp = Blueprint('drone_routes', __name__)
drone_schema = DroneSchema()
medication_schema = MedicationSchema()

@bp.route('/drones', methods=['POST'])
def create_drone():
    try:
        drone = drone_schema.load(request.json)
    except ValidationError as err:
        return err.messages, 400

    new_drone = Drone(**drone)
    db.session.add(new_drone)
    db.session.commit()
    return drone_schema.dump(new_drone), 201

from sqlalchemy.exc import IntegrityError

@bp.route('/drones/<int:id>/load', methods=['POST'])
def load_drone(id):
    drone = Drone.query.get_or_404(id)

    if drone.battery_capacity < 25:
        return jsonify({'error': 'Battery level is too low for loading'}), 400

    try:
        medications = medication_schema.load(request.json, many=True)
    except ValidationError as err:
        return err.messages, 400

    total_weight = sum(medication['weight'] for medication in medications)

    if total_weight > drone.weight_limit:
        return jsonify({'error': 'Total weight of medications exceeds the drone weight limit'}), 400

    try:
        for medication in medications:
            new_medication = Medication(**medication)
            drone.medications.append(new_medication)

        db.session.commit()
        return jsonify({'message': 'Loaded medications into drone'}), 200

    except IntegrityError as e:
        db.session.rollback()
        if 'serial_number' in str(e.orig):
            return jsonify({'error': 'Serial number already exists. Please use a different serial number.'}), 500
        else:
            return jsonify({'error': 'An unexpected database error occurred.'}), 400


@bp.route('/drones/<int:id>/medications', methods=['GET'])
def check_drone_medications(id):
    drone = Drone.query.get_or_404(id)
    return medication_schema.dump(drone.medications, many=True), 200

@bp.route('/drones/available', methods=['GET'])
def check_available_drones():
    available_drones = Drone.query.filter(Drone.state == 'IDLE').all()
    return drone_schema.dump(available_drones, many=True), 200

@bp.route('/drones/<int:id>/battery', methods=['GET'])
def check_drone_battery(id):
    drone = Drone.query.get_or_404(id)
    return jsonify({'battery_capacity': drone.battery_capacity}), 200
