import psycopg2 as psycopg2
from flask import Flask, request, jsonify, abort


DB_NAME = 'laboratory 1'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'


app = Flask(__name__)
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS region (id INT PRIMARY KEY,name VARCHAR NOT NULL);")
cur.execute("CREATE TABLE IF NOT EXISTS tax_param (id SERIAL PRIMARY KEY, city_id INT REFERENCES region(id) NOT NULL, from_hp_car INT NOT NULL, to_hp_car INT NOT NULL, from_production_year_car INT NOT NULL, to_production_year_car INT NOT NULL, rate NUMERIC NOT NULL);")
cur.execute("CREATE TABLE IF NOT EXISTS auto (id SERIAL PRIMARY KEY, city_id INT REFERENCES region(id) NOT NULL, tax_id INT REFERENCES tax_param(id) NOT NULL, name VARCHAR NOT NULL, horse_power INT NOT NULL, production_year INT NOT NULL, tax NUMERIC NOT NULL);")
conn.commit()


# Задание №1
@app.route('/v1/add/region', methods=['POST'])
def add_region():
    data = request.get_json()
    
    # извлечение параметров из полученных данных
    id = data['id']
    name = data['name']
    
    # проверка существования региона с указанным id
    cur.execute("SELECT * FROM region WHERE id=(%s)", (id,))
    region_exist = cur.fetchone()

    if region_exist:
        abort(400)
    else:
        cur.execute("INSERT INTO region (id,name) VALUES(%s,%s)", (id, name,))
        # фиксирование изменений
        conn.commit() 
        # JSON-ответ
        message = {'message': 'Region added'}
        return jsonify(message)
# Проверка: Invoke-WebRequest -Uri http://127.0.0.1:5000/v1/add/region -Method POST -Body '{"id": "54", "name": "Novosibirsk"}' -Headers @{"Content-type"="application/json"; "Accept"="application/json"}

# Задание №2
@app.route('/v1/add/tax_param', methods=['POST'])
def add_tax_param():
    data = request.get_json()

    city_id = data['city_id']
    from_hp_car = data['from_hp_car']
    to_hp_car = data['to_hp_car']
    from_production_year_car = data['from_production_year_car']
    to_production_year_car = data['to_production_year_car']
    rate = data['rate']

    # проверка наличия региона
    cur.execute("SELECT * FROM region WHERE id=(%s)", (city_id,))
    region_exist = cur.fetchone()

    if region_exist:
        cur.execute("INSERT INTO tax_param (city_id,from_hp_car,to_hp_car,from_production_year_car,to_production_year_car,rate) VALUES(%s,%s,%s,%s,%s,%s)", (city_id, from_hp_car, to_hp_car, from_production_year_car, to_production_year_car, rate))
        conn.commit()
        # JSON-ответ
        message = {'message': 'Tax_param added'}
        return jsonify(message)
    else:
        abort(400)
# Проверка: Invoke-WebRequest -Uri http://127.0.0.1:5000/v1/add/tax_param -Method POST -Body '{"city_id": "54", "from_hp_car": "100", "to_hp_car": "200", "from_production_year_car": "2000", "to_production_year_car": "2030", "rate": "5"}' -Headers @{"Content-type"="application/json"; "Accept"="application/json"}


# Задание №3
@app.route('/v1/add/auto', methods=['POST'])
def add_auto():
    data = request.get_json()

    city_id = data['city_id']
    name = data['name']
    horse_power = data['horse_power']
    production_year = data['production_year']

    cur.execute("SELECT * FROM region WHERE id=(%s)", (city_id,))
    region_exist = cur.fetchone()
    
    if region_exist:
        # проверка наличия налога для указанных характеристик автомобиля
        cur.execute("SELECT id FROM tax_param WHERE from_hp_car<=(%s) AND to_hp_car>=(%s) AND from_production_year_car<=(%s) AND to_production_year_car>=(%s)", (horse_power,horse_power,production_year,production_year,))
        tax_exist = cur.fetchone()
        
        if tax_exist:
            # вычисляется налог на автомобиль
            tax_id = int(tax_exist[0])
            cur.execute("SELECT rate FROM tax_param WHERE id=(%s)", (tax_id,))
            rate = int(cur.fetchone()[0])
            tax = rate*int(horse_power)

            cur.execute("INSERT INTO auto (city_id,tax_id,name,horse_power,production_year,tax) VALUES(%s,%s,%s,%s,%s,%s)", (city_id,tax_id,name,horse_power,production_year,tax))
            conn.commit()
            # JSON-ответ
            message = {'message': 'Auto added'}
            return jsonify(message)
        else:
            abort(400)
    else:
        abort(400)
# Проверка: Invoke-WebRequest -Uri http://127.0.0.1:5000/v1/add/auto -Method POST -Body '{"city_id": "54", "name": "Lada", "horse_power": "150", "production_year": "2010"}' -Headers @{"Content-type"="application/json"; "Accept"="application/json"}


# Задание №4
@app.route('/v1/auto/<id>', methods=['GET'])
def auto(id):
    cur.execute("SELECT * FROM auto WHERE id=(%s)", (int(id),))
    auto = cur.fetchone()
    
    # JSON-ответ
    message = {"Auto": f"{auto}"}
    return jsonify(message)

# Проверка: Invoke-WebRequest -Uri http://127.0.0.1:5000/v1/auto/1 -Method GET

# запуск flask
if __name__ == '__main__':
    app.run()
