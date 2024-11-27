from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

# Подключение к базе данных MySQL
connection = pymysql.connect(
    host='mysql', user='root', password='root', database='store_db'
)

@app.route('/products', methods=['GET'])
def get_products():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    price = data['price']
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
    connection.commit()
    return jsonify({"message": "Product added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
