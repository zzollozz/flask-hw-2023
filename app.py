import sqlite3
import secrets
from flask import Flask, request, make_response, render_template, session, redirect, url_for, flash

from authorization import is_valid_form_fields

app = Flask(__name__)
app.secret_key = bytes(secrets.token_hex(), "UTF-8")


@app.route('/')
def home():
    context = {
        'title': 'главная'
    }
    return render_template('index.html', **context)


@app.route('/products/')
def products():
    context = {
        'title': 'продукты',
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
        if is_valid_form_fields(request):
            flash('Заполните форму!', 'danger')
            return redirect(url_for('login'))

        user_email = request.form.get('email')
        password = request.form.get('password')
        # аутентификация пользователя
        # flash('Вы авторизованы!', 'success')
        session['email'] = request.form.get('email')
        session['firstname'] = request.form.get('email').split('@')[0]
        return redirect(url_for('home'))

    context = {
        'title': 'Страница входа'
    }
    return render_template('login.html', **context)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if is_valid_form_fields(request):
            flash('Заполните форму!', 'danger')
            return redirect(url_for('register'))

        # Добавление данных с формы в сессию
        for name in ['firstname', 'lastname', 'user_email', 'password']:
            session[name] = request.form.get(name)

        flash('Вы авторизованы!', 'success')
        context = {
            'tetle': 'Верификация',
            'firstname': session['firstname'],
            'lastname': session['lastname']
        }
        return render_template('verific.html', **context)

    context = {
        'title': 'Страница регистрации'
    }
    return render_template('register.html', **context)


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
