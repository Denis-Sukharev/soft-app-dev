from flask import request, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, relationship
import ast
import numpy as np
from main import db

fetch = Blueprint('fetch', __name__)

class Region(db.Model):
    __tablename__ = "region"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    car_tax_params = relationship(
        'Car_tax_param',
        backref='region',
        cascade='save-update, merge, delete'
    )

class Car_tax_param(db.Model):
    __tablename__ = "car_tax_param"
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    from_hp_car = db.Column(db.Integer, nullable=False)
    to_hp_car = db.Column(db.Integer, nullable=False)
    from_production_year_car = db.Column(db.Integer, nullable=False)
    to_production_year_car = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Float, nullable=False)

    regions = relationship(
        'Region',
        backref='car_tax_param',
        cascade='save-update, merge, delete'
    )

class Area_tax_param(db.Model):
    __tablename__ = "area_tax_param"
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    rate = db.Column(db.Float, nullable=False)

    regions = relationship(
        'Region',
        backref='area_tax_param',
        cascade='save-update, merge, delete'
    )

# 1.	Данные для эндпоинта POST /v1/region/add передаются в теле запроса
@fetch.route('/v1/region/add', methods=['POST'])
def add():
    if request.is_json:
        body = request.get_json()
        code = body['code']
        name = body['name']
        code_base = Region.query.filter_by(id=code).all()
        if code_base:
            response = {'message': 'Регион уже заполнен'}
            return jsonify(response), 400
        newRegion = Region()
        newRegion = Region(id=code,
                           name=name)
        db.session.add(newRegion)
        db.session.commit()
        return jsonify({'message': 'Успешно'})
    else:
        return jsonify({'message': 'Успешно'})

# 2.	Данные для эндпоинта POST /v1/region/update передаются в теле запроса
@fetch.route('/v1/region/update', methods=['POST'])
def update():
    if request.is_json:
        body = request.get_json()
        code = body['code']
        name = body['name']
        code_base = Region.query.filter_by(id=code).all()
        if code_base is None:
            response = {'message': 'Регион не заполнен'}
            return jsonify(response), 400
        update = Region.query.filter(Region.id == code).first()
        if update:
            update.id = code
            update.name = name
            db.session.commit()
            return jsonify({'message': 'Успешно'})

# 3.	Данные для эндпоинта POST /v1/region/delete передаются в теле запроса
@fetch.route('/v1/region/delete', methods=['POST'])
def delete():
    if request.is_json:
        body = request.get_json()
        code = body['code']
        name = body['name']
        code_base = db.session.query(Region.id, Region.name).filter(Region.id==code).all()
        if code_base is None:
            response = {'message': 'Регион не заполнен'}
            return jsonify(response), 400
        Region.query.filter(Region.id == code).delete()
        db.session.commit()
        return jsonify({'message': 'Успешно'})

# 4.	Данные для эндпоинта GET /v1/region/get передаются в GET параметрах
@fetch.route('/v1/region/get', methods=['GET'])
def getone():
    code = int(request.args.get('code'))
    code_base = db.session.query(Region.id, Region.name).filter(Region.id==code).all()
    rut = str(code_base[0])
    if code_base is None:
        response = {'message': 'Регион не заполнен'}
        return jsonify(response), 400
    else:
        return jsonify({'regiones': {
            'Данные': rut
        }}), 200

# 5.
@fetch.route('/v1/region/get/all', methods=['GET'])
def getall():
    code_base = db.session.query(Region.id, Region.name).all()
    rut = str(code_base[0])
    return jsonify({'regiones': {
        'Все данные': rut
    }}), 200
