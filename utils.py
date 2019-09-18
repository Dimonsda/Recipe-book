"""Модуль для перечислений типов блюд и единиц измерения"""
from enum import Enum


class TypesOfDish(tuple, Enum):
    """Перечисление для типов блюд"""
    SALADS_AND_APPETIZERS = ('Салаты и закуски', '/dishes/salads_and_appetizers')
    SANDWICHES = ('Бутерброды и сэндвичи', '/dishes/sandwiches')
    MEAT_DISHES = ('Блюда из мяса', '/dishes/meat_dishes')
    FISH_AND_SEAFOOD = ('Рыба и морепродукты', '/dishes/fish_and_seafood')
    SAUCES_AND_MARINADES = ('Соусы и маринады', '/dishes/sauces_and_marinades')
    VEGETABLE_DISHES = ('Блюда из овощей', '/dishes/vegetable_dishes')
    MILK_DISHES = ('Молочные блюда', '/dishes/milk_dishes')
    CEREALS_AND_PASTA = ('Крупы и макароны', '/dishes/cereals_and_pasta')
    CAKES_AND_PASTRIES = ('Торты и выпечка', '/dishes/cakes_and_pastries')
    FRUIT_DISHES = ('Блюда из фруктов', '/dishes/fruit_dishes')
    LEAN_DISHES = ('Постные блюда', '/dishes/lean_dishes')
    SWEET_FOOD_AND_DRINKS = ('Сладкие блюда и напитки', '/dishes/sweet_food_and_drinks')


class UnitsOfMeasurement(str, Enum):  # добавить еще единиц измерения (потом)
    """Перечисление для единиц измерения"""
    KILOGRAM = 'кг'
    GRAM = 'г'
    TABLE_SPOON = 'ст. л.'
    TEA_SPOON = 'ч. л.'
    LITERS = 'л'
    SHTUKI = 'шт'
