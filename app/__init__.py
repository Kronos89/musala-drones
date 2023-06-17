from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler

# Initialize Flask extensions
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

# Import the Drone model here to avoid circular import issues
from app.models.drone import Drone

def battery_check():
    drones = Drone.query.all()
    for drone in drones:
        if drone.battery_capacity < 25:
            print(f"Drone {drone.serial_number} battery level is below 25%")

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(battery_check, 'interval', minutes=5)
scheduler.start()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Initialize Flask extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from app.routes import drone_routes
    app.register_blueprint(drone_routes.bp)

    @app.cli.command('initdb')
    def initdb_command():
        """Creates the database tables."""
        db.create_all()

        # Create your default drones here
        drone1 = Drone(serial_number='12345', model='Lightweight', weight_limit=300, battery_capacity=80, state='IDLE')
        drone2 = Drone(serial_number='67890', model='Middleweight', weight_limit=400, battery_capacity=70, state='IDLE')

        db.session.add(drone1)
        db.session.add(drone2)

        db.session.commit()

        print('Initialized the database.')
    
    return app
