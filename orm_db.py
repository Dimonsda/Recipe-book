"""Бд для кулинарной книги через ORM"""
from sqlalchemy import CheckConstraint, Table

from app import db, ma
from utils import TypesOfDish, UnitsOfMeasurement

DishAndIngredient = Table('DishAndIngredient', db.metadata,
                          db.Column('dish_id', db.Integer, db.ForeignKey('Dish.Id', ondelete="CASCADE",
                                                                         onupdate="CASCADE")),
                          db.Column('ingredient_id', db.Integer, db.ForeignKey('Ingredient.Id', ondelete="CASCADE",
                                                                               onupdate="CASCADE")))

RecipeAndImplement = Table('RecipeAndImplement', db.metadata,
                           db.Column('recipe_id', db.Integer, db.ForeignKey('Recipe.Id', ondelete="CASCADE",
                                                                            onupdate="CASCADE")),
                           db.Column('implement_id', db.Integer, db.ForeignKey('Implement.Id', ondelete="CASCADE",
                                                                               onupdate="CASCADE")))


class Dish(db.Model):
    """Табличка блюда"""
    __tablename__ = 'Dish'
    __searchable__ = ['Name']
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String, nullable=False, unique=True, default="")
    Description = db.Column(db.String, nullable=False, unique=True, default="")
    Portion_count = db.Column(db.Integer, CheckConstraint('Portion_count>0'), nullable=False, default=None)
    Money = db.Column(db.Integer, nullable=False, unique=True, default="")
    Slozh = db.Column(db.String, nullable=False, unique=True, default="")
    Type_Of_Dish = db.Column(db.Enum(TypesOfDish), default=TypesOfDish.SALADS_AND_APPETIZERS)
    Recipes = db.relationship("Recipe", backref='dish')
    Ingredients = db.relationship("Ingredient", secondary=DishAndIngredient,
                                  backref=db.backref('Dishes', lazy='dynamic'))

    def __init__(self, description, name, portion_count, type_of_dish):
        self.Description = description
        self.Name = name
        self.Portion_count = portion_count
        self.Type_Of_Dish = type_of_dish

    def __repr__(self):
        return "Ingredient(%r, %r, %r, %r, %r)" % (self.Id, self.Name, self.Description, self.Portion_count,
                                                   self.Type_Of_Dish)


class Ingredient(db.Model):
    """Табличка ингредиента"""
    __tablename__ = 'Ingredient'
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String, nullable=False, default="")
    Count = db.Column(db.Integer, CheckConstraint('Count>0'), default=None)
    Unit_of_measurement = db.Column(db.Enum(UnitsOfMeasurement), default=UnitsOfMeasurement.GRAM)

    def __init__(self, count, name, unit_of_measurement):
        self.Count = count
        self.Name = name
        self.Unit_of_measurement = unit_of_measurement

    def __repr__(self):
        return "Ingredient(%r, %r, %r, %r)" % (self.Id, self.Name, self.Count, self.Unit_of_measurement)


class Implement(db.Model):
    """Табличка утвари"""
    __tablename__ = 'Implement'
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String, nullable=False, unique=True, default="")

    def __init__(self, name):
        self.Name = name

    def __repr__(self):
        return "Implement(%r, %r)" % (self.Id, self.Name)


class StepOfCook(db.Model):
    """Табличка шага приготовления"""
    __tablename__ = 'StepOfCook'
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Number_of_step = db.Column(db.Integer, CheckConstraint('Number_of_step>0'), nullable=False, default=None)
    Description = db.Column(db.String, nullable=False, unique=True, default="")
    Recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe.Id', ondelete="CASCADE", onupdate="CASCADE"),
                          nullable=False, default=None)

    def __init__(self, number_of_step, description, recipe_id):
        self.Number_of_step = number_of_step
        self.Description = description
        self.Recipe_id = recipe_id

    def __repr__(self):
        return "StepOfCook(%r, %r, %r, %r)" % (self.Id, self.Number_of_step, self.Description, self.Recipe_id)


class Recipe(db.Model):
    """Табличка рецепта"""
    __tablename__ = 'Recipe'
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Img_url = db.Column(db.String, nullable=False, unique=True, default="")
    Literature_url = db.Column(db.String, nullable=False, unique=True, default="")
    Time_on_preparation = db.Column(db.String, CheckConstraint('Time_on_preparation>0'),
                                    nullable=False, default="")
    Time_on_cooking = db.Column(db.String, CheckConstraint('Time_on_cooking>0'), nullable=False, default="")
    Dish_id = db.Column(db.Integer, db.ForeignKey('Dish.Id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False,
                        default=None)
    Steps_of_cook = db.relationship("StepOfCook", backref='recipe')
    Implements = db.relationship("Implement", secondary=RecipeAndImplement,
                                 backref=db.backref('Recipes', lazy='dynamic'))

    def __init__(self, img_url, literature_url, time_on_preparation, time_on_cooking, dish_id):
        self.Img_url = img_url
        self.Literature_url = literature_url
        self.Time_on_preparation = time_on_preparation
        self.Time_on_cooking = time_on_cooking
        self.Dish_id = dish_id

    def __repr__(self):
        return "Recipe(%r, %r, %r, %r, %r, %r)" % (self.Id, self.Img_url, self.Literature_url, self.Time_on_preparation,
                                                   self.Time_on_cooking, self.Dish_id)


class DishSchema(ma.ModelSchema):
    class Meta:
        model = Dish


class IngredientSchema(ma.ModelSchema):
    class Meta:
        model = Ingredient


class ImplementSchema(ma.ModelSchema):
    class Meta:
        model = Implement


class StepOfCookSchema(ma.ModelSchema):
    class Meta:
        model = StepOfCook


class RecipeSchema(ma.ModelSchema):
    class Meta:
        model = Recipe


dishes_schema = DishSchema(many=True)
ingredients_schema = IngredientSchema(many=True)
implements_schema = ImplementSchema(many=True)
steps_of_cook_schema = StepOfCookSchema(many=True)
recipes_schema = RecipeSchema(many=True)

db.create_all()
