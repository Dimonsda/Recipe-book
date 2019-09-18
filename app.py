"""Точка входа в приложение"""
from webbrowser import open

from flask import Flask
from flask_htmlmin import HTMLMIN
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from assets import ASSETS

APP = Flask(__name__)
APP.config.from_object('config.ProductionConfig')
ASSETS.init_app(APP)

htmlmin = HTMLMIN(APP)
db = SQLAlchemy(APP)
ma = Marshmallow(APP)
csrf = CSRFProtect(APP)

from server import *

if __name__ == '__main__':
    #open('http://localhost:5000')
    APP.run(host='0.0.0.0', port=80)
