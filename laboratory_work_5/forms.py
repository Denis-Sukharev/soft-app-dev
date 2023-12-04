from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddRegion(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Заполнить')


class Delete(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    submit = SubmitField('Удалить')


class AddTaxParam(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    city_id = StringField('city_id', validators=[DataRequired()])
    from_hp_car = StringField('from_hp_car', validators=[DataRequired()])
    to_hp_car = StringField('to_hp_car', validators=[DataRequired()])
    from_production_year_car = StringField('from_production_year_car', validators=[DataRequired()])
    to_production_year_car = StringField('to_production_year_car', validators=[DataRequired()])
    rate = StringField('rate', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class Calc(FlaskForm):
    hp_base = StringField('hp_base', validators=[DataRequired()])
    year = StringField('year', validators=[DataRequired()])
    id = StringField('id', validators=[DataRequired()])
    submit = SubmitField('Посчитать')
