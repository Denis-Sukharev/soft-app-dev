from flask import request, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, relationship
import ast
from main import db
from region_route import Region, Car_tax_param, Area_tax_param

area= Blueprint('area', __name__)

# 1.	Данные для эндпоинта POST /v1/area/tax-param/add передаются в теле запроса
@area.route('/v1/area/tax-param/add', methods=['POST'])
def add():
    if request.is_json:
        body = request.get_json()
        code = body['code']
        city_id = body['city_id']
        rate = body['rate']
        code_base = Region.query.filter_by(id=code).all()
        if code_base is None:
            response = {'message': 'Регион заполнен'}
            return jsonify(response), 400

        newArea_tax_param = Area_tax_param()
        newArea_tax_param = Area_tax_param(id=code,
                                         city_id=city_id,
                                         rate=rate,
                                         )
        db.session.add(newArea_tax_param)
        db.session.commit()
        return jsonify({'message': 'Успешно'}), 200
    else:
        return jsonify({'message': 'Успешно'})

# 2.	Данные для эндпоинта POST /v1/area/tax-param/update передаются в теле запроса
@area.route('/v1/area/tax-param/update', methods=['POST'])
def update():
    if request.is_json:
        body = request.get_json()
        code = body['code']
        city_id = body['city_id']
        rate = body['rate']
        code_base = Region.query.filter_by(id=code).all()
        if code_base is None:
            response = {'message': 'Регион заполнен'}
            return jsonify(response), 400
        update = Area_tax_param.query.filter(Area_tax_param.id == code).first()
        if update:
            update.id = code
            update.city_id = city_id
            update.rate = rate
            db.session.commit()
            return jsonify({'message': 'Успешно'}), 200

# 3.	Данные для эндпоинта POST /v1/area/tax-param/delete передаются в теле запроса
@area.route('/v1/area/tax-param/delete', methods=['POST'])
def delete():
    if request.is_json:
        body = request.get_json()
        code = body['code']
        code_base = Region.query.filter(Area_tax_param.id == code).all()
        if code_base is None:
            response = {'message': 'Регион заполнен'}
            return jsonify(response), 400
        Area_tax_param.query.filter(Area_tax_param.id == code).delete()
        db.session.commit()
        return jsonify({'message': 'Успешно'}), 200

# 4.	Данные для эндпоинта GET /v1/area/tax-param/get передаются в GET параметрах
@area.route('/v1/area/tax-param/get', methods=['GET'])
def getone():
    code = int(request.args.get('code'))
    code_base = db.session.query(Area_tax_param.id, Area_tax_param.city_id, Area_tax_param.rate).filter(Area_tax_param.id == code).all()
    rut = str(code_base[0])
    if code_base is None:
        response = {'message': 'Регион не заполнен'}
        return jsonify(response), 400
    else:
        return jsonify({'regiones': {
            'Данные': rut
        }}), 200

# 5.
@area.route('/v1/area/tax-param/get/all', methods=['GET'])
def getall():
    code_base = db.session.query(Area_tax_param.id, Area_tax_param.city_id, Area_tax_param.rate).all()
    rut = str(code_base[0])
    return jsonify({'regiones': {
        'Все данные': rut
    }}), 200

# 6.
@area.route('/v1/area/tax/calc ', methods=['GET'])
def calc():
    kadastr = int(request.args.get('kadastr'))
    code = int(request.args.get('code'))
    code_base = db.session.query(Area_tax_param.rate).filter(Area_tax_param.id == code).all()
    if code_base is None:
        response = {'message': 'Регион не заполнен'}
        return jsonify(response), 400
    object_rate = db.session.query(Area_tax_param.rate).filter(Area_tax_param.id == code).first()
    rate = float(object_rate[0])
    tax = kadastr * rate
    return jsonify({'regiones': {
        'Налог': tax
    }}), 200

