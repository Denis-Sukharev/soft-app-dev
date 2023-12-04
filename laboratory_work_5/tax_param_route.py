from flask import Blueprint, render_template
from forms import AddTaxParam, Delete
from object import Region, Car_tax_param
from dbsef import db
from flask import request

tax = Blueprint('tax', __name__)


@tax.route('/v1/car/tax-param/add', methods=['POST', 'GET'])
def add():
    form = AddTaxParam()
    if request.method == 'POST' and form.validate_on_submit(): 
        code = form.id.data
        city_id = form.city_id.data
        from_hp_car = form.from_hp_car.data
        to_hp_car = form.to_hp_car.data
        from_production_year_car = form.from_production_year_car.data
        to_production_year_car = form.to_production_year_car.data
        rate = form.rate.data
        code_base = Region.query.filter_by(id=code).all()
        if code_base is None:
            message = {'message': 'Регион не заполнен'}
            return render_template('tax-param-add.html', message=message)

        object_rate = Car_tax_param.query.filter_by(from_hp_car=from_hp_car, to_hp_car=to_hp_car,
                                                    from_production_year_car=from_production_year_car,
                                                    to_production_year_car=to_production_year_car, id=code).all()
        if object_rate:
            message = {'message': 'Заполнено'}
            return render_template('tax-param-add.html', message=message)

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
        message = 'Успешно'
    else:
        message = "Ошибка"

    return render_template('tax-param-add.html', message=message, form=form)


@tax.route('/v1/car/tax-param/update', methods=['POST', 'GET'])
def update():
    form = AddTaxParam()
    if form.validate_on_submit():
        code = form.id.data
        city_id = form.city_id.data
        from_hp_car = form.from_hp_car.data
        to_hp_car = form.to_hp_car.data
        from_production_year_car = form.from_production_year_car.data
        to_production_year_car = form.to_production_year_car.data
        rate = form.rate.data
        code_base = Region.query.filter_by(id=code).all()
        if code_base is None:
            message = 'Успешно'
            return render_template('tax-param-update.html', message=message, form=form)
        object_rate = Car_tax_param.query.filter(Car_tax_param.id == code).all()
        if object_rate is None:
            message = {'message': 'Заполнено'}
            return render_template('tax-param-update.html', message=message, form=form)
        city = Car_tax_param.query.filter(Car_tax_param.id == code).first()
        if city:
            city.id = code
            city.city_id = city_id
            city.from_hp_car = from_hp_car
            city.to_hp_car = to_hp_car
            city.from_production_year_car = from_production_year_car
            city.to_production_year_car = to_production_year_car
            city.rate = rate
            db.session.commit()
            message = 'Успешно'
            return render_template('tax-param-update.html', message=message, form=form)
    else:
        message = "Ошибка"
        return render_template('tax-param-update.html', message=message, form=form)


@tax.route('/v1/car/tax-param/delete', methods=['POST', 'GET'])
def delete():
    form = Delete()
    if form.validate_on_submit():
        code = int(form.id.data)
        code_base = Region.query.filter(Car_tax_param.id == code).all()
        if code_base is None:
            message = 'Ошибка'
            return render_template('tax-param-delete.html', message=message)
        Car_tax_param.query.filter(Car_tax_param.id == code).delete()
        db.session.commit()
        message = 'Успешно'
    else:
        message = "Ошибка"
    return render_template('tax-param-delete.html', message=message, form=form)


@tax.route('/v1/car/tax-param/get/all', methods=['GET'])
def fetch():
    code_base = db.session.query(Car_tax_param.id, Car_tax_param.city_id, Car_tax_param.from_hp_car,
                                 Car_tax_param.to_hp_car, Car_tax_param.from_production_year_car,
                                 Car_tax_param.to_production_year_car, Car_tax_param.rate).all()
    return render_template('tax-param-list.html', code_base=code_base)
