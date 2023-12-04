from flask import Blueprint, render_template
from dbsef import db
from forms import Calc
from object import Car_tax_param


tax_route = Blueprint('tax_route', __name__)


@tax_route.route('/v1/car/tax/calc', methods=['GET', 'POST'])
def calculation():
    tax = None
    form = Calc()
    if form.validate_on_submit():
        hp_base = int(form.hp_base.data)
        year = int(form.year.data)
        code = int(form.id.data)

        object_rate = db.session.query(Car_tax_param.rate).filter(Car_tax_param.from_hp_car < hp_base,
                                                                  hp_base < Car_tax_param.to_hp_car,
                                                                  Car_tax_param.from_production_year_car < year,
                                                                  year < Car_tax_param.to_production_year_car,
                                                                  Car_tax_param.id == code).first()
        rate = float(object_rate[0])
        tax = rate * hp_base
        message = tax
    else:
        message = "Ошибка"
    return render_template('index.html', message=message, form=form, tax=tax)
