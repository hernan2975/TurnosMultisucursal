from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    socketio.init_app(app)

    from app.routes.turnos import turnos_bp
    app.register_blueprint(turnos_bp)

    return app

