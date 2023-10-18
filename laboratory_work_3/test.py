# -> python laboratory_work_3\\test.py

# 1.
import requests

url = 'http://127.0.0.1:5000/v1/region/add'
body = {
    'code': 1,
    'name': 'irkutsk'
}

response = requests.post(url, json=body)

print(response.status_code)
print(response.json())

# 2.
import requests

url = 'http://127.0.0.1:5000/v1/region/update'
body = {
    'code': 1,
    'name': 'irkutsk'
}

response = requests.post(url, json=body)

print(response.status_code)
print(response.json())

# 3.
import requests

url = 'http://127.0.0.1:5000/v1/region/delete'
body = {
    'code': 2,
    'name': 'yakutia'
}

response = requests.post(url, json=body)

print(response.status_code)
print(response.json())

# 4.
import requests

url = 'http://localhost:5000/v1/region/get'
code=1

response = requests.get(f'{url}?code={code}')

automobile_data = response.json()['regiones']
print(f"tax : {automobile_data}")

# 5.
import requests

url = 'http://localhost:5000/v1/region/get/all'
id=1

response = requests.get('http://localhost:5000/v1/region/get/all')

data = response.json()['regiones']
print(f"data: {data}")

# 6.
import requests

url = 'http://127.0.0.1:5000/v1/car/tax-param/add'
body = {
    'code': 2,
    'city_id': 1,
    'from_hp_car': 200,
    'to_hp_car': 250,
    'from_production_year_car': 2005,
    'to_production_year_car': 2010,
    'rate': 2.5
}

response = requests.post(url, json=body)

print(response.status_code)
print(response.json())

# 7.
import requests

url = 'http://127.0.0.1:5000/v1/car/tax-param/update'
body = {
    'code': 2,
    'city_id': 1,
    'from_hp_car': 250,
    'to_hp_car': 300,
    'from_production_year_car': 2009,
    'to_production_year_car': 2010,
    'rate': 3.5
}

response = requests.post(url, json=body)

print(response.status_code)
print(response.json())

# 8.
import requests

url = 'http://127.0.0.1:5000/v1/car/tax-param/delete'
body = {
    'code': 1,
}

response = requests.post(url, json=body)

print(response.status_code)
print(response.json())

# 9.
import requests

url = 'http://localhost:5000/v1/car/tax-param/get'
code=2

response = requests.get(f'{url}?code={code}')

automobile_data = response.json()['regiones']
print(f"tax : {automobile_data}")

# 10.
import requests

url = 'http://localhost:5000/v1/car/tax-param/get/all'
id=1

response = requests.get('http://localhost:5000/v1/car/tax-param/get/all')

data = response.json()['regiones']
print(f"data: {data}")

# 11.
import requests

url = 'http://localhost:5000/v1/car/tax/calc'
code=2
year = 2006
hp_base = 217

response = requests.get(f'{url}?code={code}&year={year}&hp_base={hp_base}')

automobile_data = response.json()['regiones']
print(f"tax : {automobile_data}")

# 12.
import requests

url = 'http://127.0.0.1:5000/v1/area/tax-param/add'
body = {
    'code': 2,
    'city_id': 1,
    'rate': 3.5
}

response = requests.post(url, json=body)

print(response.status_code)
print(response.json())

# 13.
import requests

url = 'http://127.0.0.1:5000/v1/area/tax-param/update'
body = {
    'code': 1,
    'city_id': 1,
    'rate': 3.5
}

response = requests.post(url, json=body)

print(response.status_code)
print(response.json())

# 14.
import requests

url = 'http://127.0.0.1:5000/v1/area/tax-param/delete'
body = {
    'code': 1,
}

response = requests.post(url, json=body)

print(response.status_code)
print(response.json())

# 15.
import requests

url = 'http://localhost:5000/v1/area/tax-param/get'
code=2

response = requests.get(f'{url}?code={code}')

automobile_data = response.json()['regiones']
print(f"tax : {automobile_data}")

# 16.
import requests

url = 'http://localhost:5000/v1/area/tax-param/get/all'

response = requests.get('http://localhost:5000/v1/area/tax-param/get/all')

data = response.json()['regiones']
print(f"data: {data}")

# 17.
import requests

url = 'http://localhost:5000/v1/area/tax/calc '
code=2
kadastr = 1000

response = requests.get(f'{url}?code={code}&kadastr={kadastr}')

automobile_data = response.json()['regiones']
print(f"tax : {automobile_data}")