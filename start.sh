#!/bin/bash

echo "🔧 Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

echo "📦 Instalando dependencias..."
pip install -r requirements.txt

echo "📁 Inicializando base de datos..."
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

echo "🌱 Cargando datos de prueba..."
python seed.py

echo "🚀 Iniciando aplicación..."
python run.py
