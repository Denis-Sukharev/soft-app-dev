from flask import Flask, request, jsonify

app = Flask(__name__)

tax_rates = {}

# Задание №2
# Проверка существования региона с заданным кодов в словаре. Если нет, то добавляется кода региона и процентная ставка 
@app.route('/v1/add/tax', methods=['POST'])
def add_tax():
    data = request.json

    region_code = data.get('region_code')
    if region_code in tax_rates:
        return jsonify({'error': '400'})

    tax_rate = data.get('tax_rate')
    tax_rates[region_code] = tax_rate

    return jsonify({'message': 'Код региона и процентная ставка добавлены'})

# Проверка: Invoke-RestMethod -Uri http://localhost:5000/v1/add/tax -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"region_code":"new_region","tax_rate":15}'

# Задание №3 
# Исходные данные для проверки
tax_rates = {
    'region1': 10,
    'region2': 15,
    'region3': 20}

# 1) Выводится вся информация о налоговых ставка во всех регионах
@app.route('/v1/fetch/taxes', methods=['GET'])  
def fetch_taxes():
    return jsonify(tax_rates)

# Проверка: Invoke-RestMethod -Uri http://localhost:5000/v1/fetch/taxes -Method Get

# 2) Проверка на существование региона с заданным кодом. Если есть, то появляется информация о налоговой ставке для данного региона
@app.route('/v1/fetch/tax', methods=['GET'])
def fetch_tax():
    region_code = request.args.get('region_code')

    if region_code not in tax_rates:
        return jsonify({'error': '400'})
    
    return jsonify({'region_code': region_code, 'tax_rate': tax_rates[region_code]})

# Проверка: Invoke-RestMethod -Uri http://localhost:5000/v1/fetch/tax?region_code=region2 -Method Get

# 3) Проверка на существование региона с заданным кодом. Если есть, то возвращается сумма налога за год
@app.route('/v1/fetch/calc', methods=['GET'])
def calculate_tax():
    region_code = request.args.get('region_code')
    
    if region_code not in tax_rates:
        return jsonify({'error': '400'})

    cadastre_value = float(request.args.get('cadastre_value'))
    months_owned = int(request.args.get('months_owned'))
    annual_tax = (cadastre_value * tax_rates[region_code] * months_owned) / 12

    return jsonify({'region_code': region_code, 'annual_tax': annual_tax})

# Проверка: Invoke-RestMethod -Uri http://localhost:5000/v1/fetch/calc?region_code=new_region&cadastre_value=100000&months_owned=12 -Method Get

# Задание №4
# Передача кода и налоговой ставки региона
@app.route('/v1/update/tax', methods=['POST'])
def update_tax():
    data = request.json

    region_code = data.get('region_code')
    new_tax_rate = data.get('tax_rate')

    if region_code in tax_rates:
        tax_rates[region_code] = new_tax_rate
        return jsonify({'message': 'Код региона перезаписан'})
    else:
        return jsonify({'error': '400'})

# Проверка: Invoke-RestMethod -Uri http://localhost:5000/v1/update/tax -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"region_code":"region1","tax_rate":25}'

# @app.route('/')
# def index():
#     return 'Hello!'

if __name__ == '__main__':
    app.run(debug=True)
