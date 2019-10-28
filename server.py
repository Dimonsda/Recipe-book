"""Основной файл приложения"""
from html import escape

from flask import render_template, jsonify, request, session
import sqlite3

from app import APP
from orm_db_actions import delete_dish, get_dish_info, search_dishes_on_title
from utils import TypesOfDish, UnitsOfMeasurement


@APP.after_request
def add_http_headers(response):
    """Добавляет HTTP заголовки к каждому запросу"""
    response.headers['X-Frame-Options'] = "SAMEORIGIN"
    response.headers['X-Content-Type-Options'] = "nosniff"
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    # response.headers['Content-Security-Policy'] = "default-src 'self';" \
    #                                               "script-src 'self' 'unsafe-inline';" \
    #                                               "style-src 'self' 'unsafe-inline';" \
    #                                               "img-src 'self';" \
    #                                               "object-src 'none';" \
    #                                               "media-src 'none';" \
    #                                               "frame-src 'none';" \
    #                                               "connect-src 'self';" \
    #                                               "font-src *.google.com"
    return response


@APP.route('/delete', methods=['POST'])
def delete_dish_info():
    dish_name = escape(request.json['dish_name'])
    delete_dish(dish_name)
    return jsonify()


@APP.route('/search')
def search():
    query_title = request.args.get('query')
    dishes_info = search_dishes_on_title(query_title, session['title'])
    return render_template('dish_page.html', title=session['title'][0], types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish=session['selected_dish'], dishes_info=dishes_info)


@APP.route('/dishes/salads_and_appetizers')
def show_salads_and_appetizers():
    session['title'], session['selected_dish'] = TypesOfDish.SALADS_AND_APPETIZERS, 'Салаты и закуски'
    dishes_info = get_dish_info(TypesOfDish.SALADS_AND_APPETIZERS)
    return render_template('dish_page.html', title='Салаты и закуски', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Салаты и закуски', dishes_info=dishes_info)


@APP.route('/dishes/sandwiches')
def show_sandwiches():
    session['title'], session['selected_dish'] = TypesOfDish.SANDWICHES, 'Бутерброды и сэндвичи'
    dishes_info = get_dish_info(TypesOfDish.SANDWICHES)
    return render_template('dish_page.html', title='Бутерброды и сэндвичи', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Бутерброды и сэндвичи', dishes_info=dishes_info)


@APP.route('/dishes/meat_dishes')
def show_meat_dishes():
    session['title'], session['selected_dish'] = TypesOfDish.MEAT_DISHES, 'Блюда из мяса'
    dishes_info = get_dish_info(TypesOfDish.MEAT_DISHES)
    return render_template('dish_page.html', title='Блюда из мяса', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Блюда из мяса', dishes_info=dishes_info)


@APP.route('/dishes/fish_and_seafood')
def show_fish_and_seafood():
    session['title'], session['selected_dish'] = TypesOfDish.FISH_AND_SEAFOOD, 'Рыба и морепродукты'
    dishes_info = get_dish_info(TypesOfDish.FISH_AND_SEAFOOD)
    return render_template('dish_page.html', title='Рыба и морепродукты', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Рыба и морепродукты', dishes_info=dishes_info)


@APP.route('/dishes/sauces_and_marinades')
def show_sauces_and_marinades():
    session['title'], session['selected_dish'] = TypesOfDish.SAUCES_AND_MARINADES, 'Соусы и маринады'
    dishes_info = get_dish_info(TypesOfDish.SAUCES_AND_MARINADES)
    return render_template('dish_page.html', title='Соусы и маринады', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Соусы и маринады', dishes_info=dishes_info)


@APP.route('/dishes/vegetable_dishes')
def show_vegetable_dishes():
    session['title'], session['selected_dish'] = TypesOfDish.VEGETABLE_DISHES, 'Блюда из овощей'
    dishes_info = get_dish_info(TypesOfDish.VEGETABLE_DISHES)
    return render_template('dish_page.html', title='Блюда из овощей', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Блюда из овощей', dishes_info=dishes_info)


@APP.route('/dishes/milk_dishes')
def show_milk_dishes():
    session['title'], session['selected_dish'] = TypesOfDish.MILK_DISHES, 'Молочные блюда'
    dishes_info = get_dish_info(TypesOfDish.MILK_DISHES)
    return render_template('dish_page.html', title='Молочные блюда', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Молочные блюда', dishes_info=dishes_info)


@APP.route('/dishes/cereals_and_pasta')
def show_cereals_and_pasta():
    session['title'], session['selected_dish'] = TypesOfDish.CEREALS_AND_PASTA, 'Крупы и макароны'
    dishes_info = get_dish_info(TypesOfDish.CEREALS_AND_PASTA)
    return render_template('dish_page.html', title='Крупы и макароны', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Крупы и макароны', dishes_info=dishes_info)


@APP.route('/dishes/cakes_and_pastries')
def show_cakes_and_pastries():
    session['title'], session['selected_dish'] = TypesOfDish.CAKES_AND_PASTRIES, 'Торты и выпечка'
    dishes_info = get_dish_info(TypesOfDish.CAKES_AND_PASTRIES)
    return render_template('dish_page.html', title='Торты и выпечка', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Торты и выпечка', dishes_info=dishes_info)


@APP.route('/dishes/fruit_dishes')
def show_fruit_dishes():
    session['title'], session['selected_dish'] = TypesOfDish.FRUIT_DISHES, 'Блюда из фруктов'
    dishes_info = get_dish_info(TypesOfDish.FRUIT_DISHES)
    return render_template('dish_page.html', title='Блюда из фруктов', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Блюда из фруктов', dishes_info=dishes_info)


@APP.route('/dishes/lean_dishes')
def show_lean_dishes():
    session['title'], session['selected_dish'] = TypesOfDish.LEAN_DISHES, 'Постные блюда'
    dishes_info = get_dish_info(TypesOfDish.LEAN_DISHES)
    return render_template('dish_page.html', title='Постные блюда', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Постные блюда', dishes_info=dishes_info)


@APP.route('/dishes/sweet_food_and_drinks')
def show_sweet_food_and_drinks():
    session['title'], session['selected_dish'] = TypesOfDish.SWEET_FOOD_AND_DRINKS, 'Сладкие блюда и напитки'
    dishes_info = get_dish_info(TypesOfDish.SWEET_FOOD_AND_DRINKS)
    return render_template('dish_page.html', title='Сладкие блюда', types_of_dish=TypesOfDish,
                           units_of_measurement=UnitsOfMeasurement,
                           selected_dish='Сладкие блюда', dishes_info=dishes_info)


@APP.route('/')
def show_first_page():
    return render_template('first_page.html', title='Кулинарная книга', types_of_dish=TypesOfDish)


@APP.route('/about')
def show_about():
    return render_template('about.html', title='О проекте', types_of_dish=TypesOfDish)


@APP.route('/login', methods=['GET', 'POST'])
def show_login():
    message = ''
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT login FROM users WHERE login = ?", (username,))
        userlist = cursor.fetchone();
        cursor.execute("SELECT pass FROM users WHERE login = ?", (username,))
        passlist = cursor.fetchone();

        print(username)
        print(userlist)
        print(passlist)

        if userlist[0] != "None":
            if username == userlist[0] and password == passlist[0]:
                print("kaef")
                return render_template('first_page.html', title='Кулинарная книга', types_of_dish=TypesOfDish)
#            message = "Correct username and password"

#            print(username)
        else:
            message = "Wrong username or password"

#            print(userlist[0])
#            print(username)
#
        cursor.close()
        conn.commit()
        conn.close()
    return render_template('login.html', message=message)


@APP.route('/reg', methods=['GET', 'POST'])
def show_reg():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        sql = 'INSERT INTO users (login, pass) VALUES (?, ?);'
        cursor.execute(sql, (username, password))

        cursor.close()
        conn.commit()
        conn.close()
    return render_template('login.html',title='Вход')
# ToDo - сделать всплывающие формы для редактирования и добавления

