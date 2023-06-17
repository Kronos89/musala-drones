import unittest
from flask import json
from app import create_app, db
from app.models.drone import Drone

class DroneModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_drone_model(self):
        d = Drone(serial_number='serial1', model='Lightweight', weight_limit=500, battery_capacity=100, state='IDLE')
        db.session.add(d)
        db.session.commit()

        self.assertEqual(Drone.query.count(), 1)

    def test_drone_route(self):
        d = Drone(serial_number='serial2', model='Lightweight', weight_limit=500, battery_capacity=100, state='IDLE')
        db.session.add(d)
        db.session.commit()

        response = self.app.test_client().get('/drones')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)

if __name__ == '__main__':
    unittest.main()
