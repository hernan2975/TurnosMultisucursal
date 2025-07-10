
from flask import Blueprint, render_template
from app.models.models import Turno, Profesional, Sucursal
from app import db

turnos_bp = Blueprint("turnos", __name__, url_prefix="/")

@turnos_bp.route("/")
def index():
    turnos = Turno.query.all()
    return render_template("base.html", turnos=turnos)
