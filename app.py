import sqlite3

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'title': 'главная'
    }
    return render_template('index.html', **context)


@app.route('/products/')
def products():
    context = {
        'title': 'продукты'
    }
    return render_template('products.html', **context)


@app.route('/product/')
# @app.route('/products/<int:id>/')    # Все продукты - Витрина
def product(id=1):
    product = {
        'id': id,
        'name': 'text Product',
        'category': 'text Category',
        'price': 3411.00,
        'shot_desc': 'тест описание',
        'description': 'тестовое подробное описание'

    }
    context = {
        'title': 'карточка продукта',
        'cart_prod': id,
        'product': product,

    }
    return render_template('product.html', **context)


@app.route('/contact/')
def contact():
    context = {
        'title': 'Контакты',
    }
    return render_template('contact.html', **context)


@app.route('/clothes/')  # Одежда
def clothes():
    context = {
        'title': 'Одежда',
    }
    return render_template('clothes.html', **context)


@app.route('/footwear/')  # Обувь
def footwear():
    context = {
        'title': 'Обувь'
    }
    return render_template('footwear.html', **context)


@app.route('/jacket/')  # Куртка
def jacket():
    context = {
        'title': 'Куртка'
    }
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run()
