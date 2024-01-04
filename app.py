import sqlite3

from flask import Flask, request, redirect, url_for
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

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        user_email = request.form.get('email')
        # аутентификация пользователя
        return redirect(url_for('home'))

    context = {
        'title': 'Страница входа'
    }
    return render_template('login.html', **context)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        user_email = request.form.get('email')
        password = request.form.get('password')

        # Запись данных о пользователе в базу данных
        return redirect(url_for('home'))

    context = {
        'title': 'Страница регистрации'
    }
    return render_template('register.html', **context)


if __name__ == '__main__':
    app.run()
