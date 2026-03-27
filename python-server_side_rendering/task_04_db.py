from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sql(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if product_id is not None:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        return None


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if product_id is not None:
        product_id = int(product_id)

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql(product_id)
        if data is None:
            return render_template('product_display.html', error="Database error occurred.")
        if product_id is not None and not data:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=data)
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
