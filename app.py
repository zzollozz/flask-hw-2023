import hashlib

from flask import request, render_template, session, redirect, url_for, flash

from authorization import is_valid_form_fields
from conf import app, db
from models import Users
from forms import RegistrationForm, LoginForm


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
def product():
    product = {
        'id': 00,
        'name': 'Jordan 1 Retro High Game Royal',
        'category': 'обувь',
        'price': 43045.00,
        'shot_desc': 'Бренд: Air Jordan',
        'description': 'Модель: AIR JORDAN 1 RETRO HIGH OG "GAME ROYAL"'

    }
    context = {
        'title': 'карточка продукта',
        'cart_prod': 00,
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
        'name': 'Vidda Pro Wool Padded Jacket M',
        'category': 'Куртка',

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
        'title': 'Куртка',
        'name_page': 'Большой выбор курток'
    }
    return render_template('jacket.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        data_user = Users.query.filter_by(user_login=form.user_login.data).first()
        password = hashlib.sha256(form.password.data.encode('utf-8')).hexdigest()
        # аутентификация пользователя
        if data_user and password == data_user.password:

            # Нужно понять что хранить в открытой ссесии !!!!!!!!!!!!
            session['user_login'] = data_user.user_login
            return redirect(url_for('home'))
        else:
            flash('Пройдите регистрацию', 'warning')
            return redirect(url_for('login'))
    context = {
        'title': 'Страница входа'
    }
    return render_template('login.html', **context, form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST' and form.validate():
        data_user = Users(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            user_login=form.user_login.data,
            gender=form.gender.data,
            email=form.email.data,
            password=hashlib.sha256(form.password.data.encode('utf-8')).hexdigest()
        )
        db.session.add(data_user)
        db.session.commit()
        session['user_login'] = data_user.user_login
        context = {
            'title': 'Верификация',
            'firstname': data_user.firstname,
            'lastname': data_user.lastname
        }
        return render_template('verific.html', **context)

    context = {
        'title': 'Страница регистрации',
    }
    return render_template('register.html', **context, form=form)


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run()
