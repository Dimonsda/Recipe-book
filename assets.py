"""Генерация CSS, JS файлов в один"""
from flask_assets import Environment, Bundle

bundles = {
    'jquery_custom_scripts': Bundle(
        'js/libs/jquery_js/jquery-3.3.1.min.js',
        'js/page_links.js',
        'js/main.js',
        output='gen/jquery_custom_scripts.js',
        filters='jsmin'),
    'popper_bootstrap_jquery-confirm_js': Bundle(
        'js/libs/popper_js/popper.min.js',
        'js/libs/bootstrap_js/bootstrap.min.js',
        'js/libs/jquery-confirm_js/jquery-confirm.min.js',
        output='gen/popper_bootstrap_jquery-confirm.js',
        filters='jsmin'),
    'jquery-confirm_fontawesome_custom_css': Bundle(
        'css/libs/jquery-confirm_css/jquery-confirm.min.css',
        # 'css/libs/fontawesome_css/font-awesome.min.css',
        'css/first_page_style.css',
        output='gen/jquery-confirm_fontawesome_custom.css',
        filters='cssmin')
}
ASSETS = Environment()
ASSETS.register(bundles)
