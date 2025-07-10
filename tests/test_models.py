from app.models.models import Sucursal, Profesional

def test_sucursal_creation(app):
    sucursal = Sucursal(nombre="Sucursal Central", direccion="Av. Siempreviva 123")
    assert sucursal.nombre == "Sucursal Central"
    assert sucursal.direccion.startswith("Av.")

def test_profesional_email_field(app):
    profe = Profesional(nombre="Dra. Ana", especialidad="Dermatología", email="ana@example.com", sucursal_id=1)
    assert "@" in profe.email

