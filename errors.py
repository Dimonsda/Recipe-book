"""Модуль для обработки ошибок на веб-страницах"""
from flask import render_template
from flask_wtf.csrf import CSRFError

from server import APP


@APP.errorhandler(404)
def not_found_error(error):
    """Эта функция вызывает пользовательскую страницу искл-я для ошибки 404 Not Found"""
    return render_template('404.html', reason=error.description), 404


@APP.errorhandler(500)
def internal_server_error(error):
    """Эта функция вызывает пользовательскую страницу искл-я для ошибки 500 Internal Server Error"""
    return render_template('500.html', reason=error.description), 500


@APP.errorhandler(CSRFError)
def handle_csrf_error(error):
    """Эта функция обрабатывает ошибку CSRF валидации"""
    return render_template('csrf_error.html', reason=error.description), 400
