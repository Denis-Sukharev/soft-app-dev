from flask import Flask
from routes import users
from dbase import db, login_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/LR6'
app.config['SQLAlchemy_TRACK_MODIFIVATTION'] = False
db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(users)

if __name__ == "__main__":
   app.run(debug=True)

# create table profile
# (id serial primary key,
#  email varchar (100) not null,
#  password varchar (1000) not null,
#  name varchar not null);
   