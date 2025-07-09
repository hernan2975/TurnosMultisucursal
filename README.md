# 🏥 TurnosMultisucursal

Plataforma web modular para la gestión de turnos en empresas con múltiples sucursales. Ideal para clínicas, laboratorios, estudios profesionales u ópticas. Desarrollado con **Python (Flask)** y **JavaScript**, incorpora actualizaciones en tiempo real, estructura escalable y panel administrativo con métricas.

---

## 🚀 Características Principales

- ✅ CRUD completo de **sucursales**, **profesionales**, y **servicios**
- 📅 Reserva de turnos por **tipo de servicio** y **ubicación**
- 🔁 WebSockets para **actualizaciones en tiempo real**
- 📊 Panel administrativo con **dashboard de métricas**
- 🔧 Arquitectura modular con **Flask Blueprints**
- 🔌 Preparado para integración con **APIs externas** (ej.: ARASAAC para accesibilidad)

---

## 🧩 Tecnologías Usadas

| Backend         | Frontend     | Base de datos | Otros           |
|----------------|--------------|---------------|-----------------|
| Flask (Python) | HTML, CSS    | SQLite        | Socket.IO       |
| Flask-SQLAlchemy | JavaScript | PostgreSQL (opcional) | Jinja2 Templates |

---

## 🛠️ Instalación Local

```bash
# 1. Clonar el repositorio
git clone https://github.com/usuario/TurnosMultisucursal.git
cd TurnosMultisucursal

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear base de datos local
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

# 5. Ejecutar servidor
python run.py

🧪 Testing
El proyecto incluye estructura para agregar tests con pytest. Para ejecutar los tests:

pytest

📁 Estructura del Proyecto

TurnosMultisucursal/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
├── migrations/
├── requirements.txt
├── run.py
├── README.md

📦 Roadmap
🧠 Autenticación con Flask-Login y autorización por roles

📱 Diseño responsive con Bootstrap o TailwindCSS

🌐 Integración con API de pictogramas para accesibilidad

🧩 Dockerización y despliegue CI/CD

🤝 Contribuciones
Las contribuciones están abiertas. Se agradece especialmente:

Mejoras en accesibilidad

Integración de APIs locales o internacionales

Componentes UI reutilizables

🧾 Licencia
Este proyecto se distribuye bajo la MIT License. Ver el archivo LICENSE para más detalles.

✨ Autor
Hernán Luis Lang Desarrollador Full Stack con enfoque en accesibilidad, modularidad y soluciones escalables.
