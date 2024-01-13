import secrets

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.secret_key = bytes(secrets.token_hex(), "UTF-8")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testshop.db'
app.config['SECRET_KEY'] = app.secret_key

csrf = CSRFProtect(app)
db = SQLAlchemy(app)
