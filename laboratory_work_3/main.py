from flask import Flask, request, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from main import db
from region_route import fetch
from area_route import area
from car_route import car

# Запуск локального сервера Flask 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/lab3'
app.config['SQLAlchemy_TRACK_MODIFIVATTION'] = False

# Инициализация расширения SQLAlchemy
db.init_app(app)

# Регистрация локального сервера Flask 
app.register_blueprint(fetch)
app.register_blueprint(car)
app.register_blueprint(area)

if __name__ == "__main__":
    app.run(debug=True)

