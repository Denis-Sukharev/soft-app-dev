import psycopg2 as psycopg2

DB_NAME = 'lab3'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS region (id SERIAL PRIMARY KEY, name VARCHAR NOT NULL);")
cur.execute("CREATE TABLE IF NOT EXISTS car_tax_param (id SERIAL PRIMARY KEY, city_id INT REFERENCES region(id) NOT NULL, from_hp_car INT NOT NULL, to_hp_car INT NOT NULL, from_production_year_car INT NOT NULL, to_production_year_car INT NOT NULL, rate NUMERIC NOT NULL);")
cur.execute("CREATE TABLE IF NOT EXISTS auto (id SERIAL PRIMARY KEY, city_id INT REFERENCES region(id) NOT NULL, tax NUMERIC NOT NULL);")
conn.commit()
