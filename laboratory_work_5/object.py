from sqlalchemy.orm import relationship
from dbsef import db

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    car_tax_param = relationship(
        'Car_tax_param',
        backref='city',
        cascade='save-update, merge, all, delete, delete-orphan'
    )


class Car_tax_param(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    from_hp_car = db.Column(db.Integer, nullable=False)
    to_hp_car = db.Column(db.Integer, nullable=False)
    from_production_year_car = db.Column(db.Integer, nullable=False)
    to_production_year_car = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Float, nullable=False)
