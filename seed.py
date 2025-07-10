from app import create_app, db
from app.models.models import Sucursal, Profesional, Turno

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    s1 = Sucursal(nombre="Sucursal Centro", direccion="Av. San Martín 123")
    s2 = Sucursal(nombre="Sucursal Norte", direccion="Ruta 7 Km 5")

    db.session.add_all([s1, s2])
    db.session.commit()

    p1 = Profesional(nombre="Dra. Gómez", especialidad="Dermatología", email="gomez@clinic.com", sucursal_id=s1.id)
    p2 = Profesional(nombre="Lic. Paredes", especialidad="Nutrición", email="paredes@clinic.com", sucursal_id=s2.id)

    db.session.add_all([p1, p2])
    db.session.commit()

    t1 = Turno(fecha="2025-07-10", hora="10:00", sucursal_id=s1.id, profesional_id=p1.id)
    t2 = Turno(fecha="2025-07-10", hora="11:00", sucursal_id=s2.id, profesional_id=p2.id)

    db.session.add_all([t1, t2])
    db.session.commit()

    print("✅ Base de datos poblada exitosamente.")

