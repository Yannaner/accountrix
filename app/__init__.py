from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

socketio = SocketIO()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    socketio.init_app(app)

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
