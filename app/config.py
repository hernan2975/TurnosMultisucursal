import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "devkey")
    SQLALCHEMY_DATABASE_URI = "sqlite:///turnos.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

