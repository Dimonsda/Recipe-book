"""Файл конфигурации проекта"""
from os import path
basedir = path.abspath(path.dirname(__file__))


class Config(object):
    """Основной класс конфигурации"""
    DEBUG = False
    #CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'dffgrtrw45'
    SECRET_KEY = 'NotTellAnyone'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'cooking_book.db')
    SESSION_COOKIE_HTTPONLY = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MINIFY_PAGE = True


class ProductionConfig(Config):
    """Конфигурация для выпуска в Production"""
    ASSETS_DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    """Конфигурация для отладки"""
    DEBUG = False
    ASSETS_DEBUG = True
