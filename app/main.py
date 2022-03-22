"""app.main

Module that starts the Flask application
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# pylint: disable=C0103
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from app.healthcheck import blueprint as health_check_blueprint
from app.tasks import blueprint as tasks_blueprint



app.register_blueprint(health_check_blueprint.create_blueprint())
app.register_blueprint(tasks_blueprint.create_blueprint())

db.create_all()