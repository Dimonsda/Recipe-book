"""Модуль базы данных sqlite для приложения"""
from sqlite3 import connect

CONN = connect('cooking_book.db')

CURSOR = CONN.cursor()

CURSOR.execute("""PRAGMA foreign_keys = ON""")

CURSOR.execute("""CREATE TABLE if not exists dish
                (id integer PRIMARY KEY AUTOINCREMENT,
                name text NOT NULL, description text NOT NULL,
                portion_count integer CHECK (portion_count>0) NOT NULL,
                type_of_dish text NOT NULL,
                money integer NOT NULL,
                complexity text NOT NULL,
                CONSTRAINT unique_name_and_description UNIQUE (name, description))""")

CURSOR.execute("""CREATE TABLE if not exists ingredient
                (id integer PRIMARY KEY AUTOINCREMENT,
                name text NOT NULL, count integer CHECK (count>0),
                unit_of_measurement text NOT NULL)""")

CURSOR.execute("""CREATE TABLE if not exists implement
                (id integer PRIMARY KEY AUTOINCREMENT,
                name text NOT NULL,
                CONSTRAINT unique_name UNIQUE (name))""")

CURSOR.execute("""CREATE TABLE if not exists step_of_cook
                (id integer PRIMARY KEY AUTOINCREMENT,
                number_of_step integer CHECK (number_of_step>0) NOT NULL,
                description text NOT NULL, recipe_id integer NOT NULL,
                FOREIGN KEY (recipe_id) REFERENCES recipe(id) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT unique_description UNIQUE (description))""")

CURSOR.execute("""CREATE TABLE if not exists recipe
                (id integer PRIMARY KEY AUTOINCREMENT,
                img_url text NOT NULL, literature_url text NOT NULL,
                time_on_preparation text CHECK (time_on_preparation>0) NOT NULL,
                time_on_cooking text CHECK (time_on_cooking>0) NOT NULL,
                dish_id integer NOT NULL,
                FOREIGN KEY (dish_id) REFERENCES dish(id) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT unique_urls UNIQUE (img_url, literature_url))""")

CURSOR.execute("""CREATE TABLE if not exists recipe_and_implement
                (recipe_id integer NOT NULL, implement_id integer NOT NULL,
                FOREIGN KEY (recipe_id) REFERENCES recipe(id) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (implement_id) REFERENCES implement(id) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT composite_key_2 PRIMARY KEY (recipe_id, implement_id))""")

CURSOR.execute("""CREATE TABLE if not exists dish_and_ingredient
                (dish_id integer NOT NULL, ingredient_id integer NOT NULL,
                FOREIGN KEY (dish_id) REFERENCES dish(id) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (ingredient_id) REFERENCES ingredient(id) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT composite_key_1 PRIMARY KEY (dish_id, ingredient_id))""")

CONN.commit()
CONN.close()
