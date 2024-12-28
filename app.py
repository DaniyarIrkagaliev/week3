from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Обработчик для всех методов по CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'x-test, ngrok-skip-browser-warning, Content-Type, Accept, Access-Control-Allow-Headers')
    return response

# Маршрут для обработки запросов к /result4/
@app.route('/result4/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def result():
    # Получаем значение заголовка x-test
    x_test_value = request.headers.get('x-test')
    
    # Получаем тело запроса
    body = request.data.decode()
    
    # Формируем JSON-ответ
    response_data = {
        'message': 'itmo413764',
        'x-result': x_test_value,
        'x-body': body
    }
    
    # Преобразуем данные в JSON и возвращаем их
    response_json = jsonify(response_data)
    response_json.headers['Content-Type'] = 'application/json'
    
    return response_json

if __name__ == '__main__':
    app.run(debug=True)
