# Musala Soft Drones Test

Welcome to the Musala Soft Drones Test project! This is a Flask-based web application that allows users to manage a fleet of drones and load them with medications for delivery.
Prerequisites

Before you can run this project, you must have the following installed on your computer:

    Python 3.x
    Flask
    SQLAlchemy

Installation

To install this project, follow these steps:

    Clone the repository to your local machine:

git clone https://github.com/Kronos89/musala-drones
```

Navigate to the project directory:

cd musala-drones
```

Create a virtual environment for the project:

python3 -m venv venv
```

Activate the virtual environment:

source venv/bin/activate
```

Install the project dependencies:
basic

pip install -r requirements.txt
```

Create the database and initialize it with sample data:

    flask initdb
    flask db migrate
    flask db upgrade

Usage

To run the project, activate the virtual environment and run the Flask development server:
routeros

source venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

You can then access the web application by navigating to http://localhost:5000 in your web browser.
Features

This web application allows users to perform the following actions:

    View a list of all drones in the fleet.
    View details of a specific drone, including its current state and battery level.
    Load a drone with medications for delivery.
    View a list of all medications in the system.
    View details of a specific medication, including its weight and serial number.
    Search for medications by name or code.
    View a list of all deliveries that have been completed.
    View details of a specific delivery, including the drone that was used and the medications that were delivered.

Contributing

If you would like to contribute to this project, please follow these steps:

    Fork the repository on GitHub.
    Create a new branch for your changes.
    Make your changes and commit them with descriptive commit messages.
    Push your changes to your forked repository.
    Submit a pull request to the original repository.

Credits

This project was created by Reynier Vega for the Musala Soft Drones Test. It is licensed under the MIT License.
