from region_route import region
from tax_param_route import tax
from tax_route import tax_route
from dbsef import db, app

app.config['SECRET_KEY'] = 'test'
db.init_app(app)

app.register_blueprint(region)
app.register_blueprint(tax)
app.register_blueprint(tax_route)

if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
    app.run(debug=True, host='0.0.0.0', port='4567')




