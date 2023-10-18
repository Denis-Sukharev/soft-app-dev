from flask import request, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, relationship
import ast
from main import db
from region_route import Region, Car_tax_param, Area_tax_param

car = Blueprint('car', __name__)

# 1.	Данные для эндпоинта POST /v1/car/tax-param/add передаются в теле запроса
@car.route('/v1/car/tax-param/add', methods=['POST'])
def add():
    if request.is_json:
        body = request.get_json()
        code = body['code']
        city_id = body['city_id']
        from_hp_car = body['from_hp_car']
        to_hp_car = body['to_hp_car']
        from_production_year_car = body['from_production_year_car']
        to_production_year_car = body['to_production_year_car']
        rate = body['rate']
        code_base = Region.query.filter_by(id=code).all()
        if code_base is None:
            response = {'message': 'Регион не заполнен'}
            return jsonify(response), 400
        object_rate = Car_tax_param.query.filter_by(from_hp_car = from_hp_car, to_hp_car = to_hp_car, from_production_year_car = from_production_year_car, to_production_year_car = to_production_year_car, id = code).all()
        if object_rate:
            response = {'message': 'Заполнено'}
            return jsonify(response), 400
        newCar_tax_param = Car_tax_param()
        newCar_tax_param = Car_tax_param(id=code,
                                         city_id=city_id,
                                         from_hp_car=from_hp_car,
                                         to_hp_car=to_hp_car,
                                         from_production_year_car=from_production_year_car,
                                         to_production_year_car=to_production_year_car,
                                         rate=rate
                                         )
        db.session.add(newCar_tax_param)
        db.session.commit()
        return jsonify({'message': 'Успешно'})
    else:
        return jsonify({'message': 'Успешно'})

# 2.	Данные для эндпоинта POST /v1/car/tax-param/update передаются в теле запроса
@car.route('/v1/car/tax-param/update', methods=['POST'])
def update():
    if request.is_json:
        body = request.get_json()
        code = body['code']
        city_id = body['city_id']
        from_hp_car = body['from_hp_car']
        to_hp_car = body['to_hp_car']
        from_production_year_car = body['from_production_year_car']
        to_production_year_car = body['to_production_year_car']
        rate = body['rate']
        code_base = Region.query.filter_by(id=code).all()
        if code_base is None:
            response = {'message': 'Регион не заполнен'}
            return jsonify(response), 400
        object_rate = Car_tax_param.query.filter(Car_tax_param.id==code).all()
        print(object_rate)
        if object_rate is None:
            response = {'message': 'Не заполнено'}
            return jsonify(response), 400
        update = Car_tax_param.query.filter(Car_tax_param.id == code).first()
        if update:
            update.id = code
            update.city_id = city_id
            update.from_hp_car = from_hp_car
            update.to_hp_car = to_hp_car
            update.from_production_year_car = from_production_year_car
            update.to_production_year_car = to_production_year_car
            update.rate = rate
            db.session.commit()
            return jsonify({'message': 'Успешно'})

# 3.	Данные для эндпоинта POST /v1/car/tax-param/delete передаются в теле запроса
@car.route('/v1/car/tax-param/delete', methods=['POST'])
def delete():
    if request.is_json:
        body = request.get_json()
        code = body['code']
        code_base = Region.query.filter(Car_tax_param.id==code).all()
        if code_base is None:
            response = {'message': 'Регион не заполнен'}
            return jsonify(response), 400
        Car_tax_param.query.filter(Car_tax_param.id == code).delete()
        db.session.commit()
        return jsonify({'message': 'Успешно'})

# 4.	Данные для эндпоинта GET /v1/car/tax-param/get передаются в GET параметрах
@car.route('/v1/car/tax-param/get', methods=['GET'])
def getone():
    code = int(request.args.get('code'))
    code_base = db.session.query(Car_tax_param.id, Car_tax_param.city_id, Car_tax_param.from_hp_car, Car_tax_param.to_hp_car, Car_tax_param.from_production_year_car, Car_tax_param.to_production_year_car, Car_tax_param.rate).filter(Car_tax_param.id == code).all()
    rut = str(code_base[0])
    if code_base is None:
        response = {'message': 'Регион не заполнен'}
        return jsonify(response), 400
    else:
        return jsonify({'regiones': {
            'Данные': rut
        }}), 200

# 5.	Данные для эндпоинта GET /v1/car/tax/calc передаются в GET параметрах
@car.route('/v1/car/tax/calc', methods=['GET'])
def calc():
    hp_base = int(request.args.get('hp_base'))
    year = int(request.args.get('year'))
    code = int(request.args.get('code'))

    object_rate = db.session.query(Car_tax_param.rate).filter(Car_tax_param.from_hp_car < hp_base, hp_base < Car_tax_param.to_hp_car,
                                                Car_tax_param.from_production_year_car < year, year < Car_tax_param.to_production_year_car,
                                                Car_tax_param.id == code).first()
    rate = float(object_rate[0])
    tax = rate * hp_base

    return jsonify({'regiones': {
        'Налог': tax
    }}), 200

# 6.	Данные для эндпоинта GET /v1/car/tax-param/get/all передаются в GET параметрах
@car.route('/v1/car/tax-param/get/all', methods=['GET'])
def getall():
    code_base = db.session.query(Car_tax_param.id, Car_tax_param.city_id, Car_tax_param.from_hp_car, Car_tax_param.to_hp_car, Car_tax_param.from_production_year_car, Car_tax_param.to_production_year_car, Car_tax_param.rate).all()
    rut = str(code_base)
    return jsonify({'regiones': {
        'Все данные': rut
    }}), 200