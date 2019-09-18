from sqlalchemy import and_

from app import db
from orm_db import Dish


def delete_dish(dish_name):
    """Удаление информации о блюде из БД по его имени"""
    db.session.query(Dish).filter_by(Name=dish_name).delete()
    db.session.flush()
    db.session.commit()


def get_dish_info(dish_type):
    """Получение блюд, соответствующих типу dish_type"""
    dishes_info = db.session.query(Dish).filter_by(Type_Of_Dish=dish_type).all()
    return dishes_info


def search_dishes_on_title(query_title, dish_type):
    """Поиск по названию блюда"""
    dishes = db.session.query(Dish).filter(and_(Dish.Name.like('%' + query_title + '%'),
                                                Dish.Type_Of_Dish.like(dish_type))).all()
    return dishes
