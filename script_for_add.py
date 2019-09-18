from app import db
from orm_db import Dish, Implement, Ingredient, Recipe, StepOfCook
from utils import TypesOfDish, UnitsOfMeasurement

dish = Dish("Беспроигрышный вариант накормить гостей за праздничным столом - "
            "запечь курицу целиком в духовке. Блюдо смотрится богато и "
            "аппетитно! Птицу замаринуйте в соевом маринаде, затем смажьте "
            "творожным сыром.", "Курица с сыром в духовке (Жар птица)", 6, TypesOfDish.MEAT_DISHES)
db.session.add(dish)
db.session.flush()
db.session.commit()

recipe = Recipe("/static/img/kurica_s_sirom_v_duhovke.jpg", "https://povar.ru/recipes"
                                                            "/kurica_s_syrom_v_duhovke_jar_ptica-72195.html",
                "30 мин.", "2 ч.", 1)
db.session.add(recipe)
db.session.flush()
db.session.commit()

ingredient = Ingredient(3, "Курица", UnitsOfMeasurement.KILOGRAM)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(2, "Соевый соус", UnitsOfMeasurement.TABLE_SPOON)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(2, "Горчица", UnitsOfMeasurement.TABLE_SPOON)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(2, "Масло растительное", UnitsOfMeasurement.TABLE_SPOON)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(1, "Чеснок сушеный", UnitsOfMeasurement.TABLE_SPOON)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(150, "Сыр творожный", UnitsOfMeasurement.GRAM)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

implement = Implement("Бумажные полотенца")
recipe.Implements.append(implement)
db.session.add(implement)
db.session.flush()
db.session.commit()

implement = Implement("Противень")
recipe.Implements.append(implement)
db.session.add(implement)
db.session.flush()
db.session.commit()

implement = Implement("Пергамент для выпечки")
recipe.Implements.append(implement)
db.session.add(implement)
db.session.flush()
db.session.commit()

implement = Implement("Деревянные шпажки")
recipe.Implements.append(implement)
db.session.add(implement)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(1, "Выпотрошенную тушку курицы промойте под холодной водой, обсушите бумажными полотенцами. "
                             "Соедините соевый соус, горчицу и растительное масло. Натрите смесью птицу внутри и "
                             "снаружи. Оставьте мариноваться на 20 минут.", 1)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(2, "Курицу разрежьте по грудке и разверните, как на фото. Натрите сушенным чесноком. "
                             "Поместите курицу на противень с пергаментом для выпечки.", 1)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(3, "Смажьте верх птицы творожным сыром с зеленым луком. Поставьте запекаться в разогретую "
                             "до 200 градусов духовку на 30 минут. Уменьшите температуру до 180 градусов и "
                             "продолжайте запекать курицу до готовности. Время готовки зависит от веса курицы. У меня "
                             "заняло 1,5 часа.", 1)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(4, "Проверьте курицу на готовность: проткните мясо деревянной шпажкой, выделившийся сок "
                             "должен быть прозрачным.", 1)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(5, "Подавайте 'Жар птицу' с отварным рисом, свежей зеленью и овощами. Приятного аппетита!", 1)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

dish = Dish("На новогодние праздники не забудьте удивить своих маленьких непосед. Забавное "
            "печенье обязательно им понравится. Печенье в виде мордашки собаки легко испечь "
            "вместе с детьми, без специальной формочки.", "Печенье Мордашки", 8, TypesOfDish.SWEET_FOOD_AND_DRINKS)
db.session.add(dish)
db.session.flush()
db.session.commit()

recipe = Recipe("/static/img/pechenie_mordashki.jpg", "https://povar.ru/recipes/pechene_mordashki-65369.html",
                "30 мин.", "1 ч. 30 мин", 2)
db.session.add(recipe)
db.session.flush()
db.session.commit()

ingredient = Ingredient(280, "Мука", UnitsOfMeasurement.GRAM)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(200, "Масло сливочное", UnitsOfMeasurement.GRAM)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(100, "Сахар", UnitsOfMeasurement.GRAM)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(1, "Какао-порошок", UnitsOfMeasurement.TABLE_SPOON)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(10, "Шоколадные капли", UnitsOfMeasurement.GRAM)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

implement = Implement("Измельчитель")
recipe.Implements.append(implement)
db.session.add(implement)
db.session.flush()
db.session.commit()

implement = Implement("Духовка")
recipe.Implements.append(implement)
db.session.add(implement)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(1, "Подготовьте необходимые продукты. Для белого теста: 150 г муки, 100 г сливочного масла, "
                             "50 г сахара.", 2)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(2, "Для шоколадного теста: 130 г муки, какао - 1 ст. л.,"
                             " 100 г сливочного масла, 50 г сахара.", 2)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(3, "Сахар и масло взбейте в измельчителе до однородной массы, добавьте просеянную муку, "
                             "перемешивайте только тех пор, пока тесто не начнет собираться в комок. Также замесите "
                             "шоколадное тесто. Накройте пищевой пленкой и оставьте в холодильнике на 1 час.", 2)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(4, "Белое тесто разделите на 16 равных частей. Скатайте жгутики и сверните их спиралью.", 2)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(5, "Шоколадное тесто раскатайте в пласт, толщиной 5 мм. Вырубите кружки для мордочек, "
                             "глаз и носиков (по желанию их можно заменить на шоколадные капли). Ушки-треугольники "
                             "прилепите к мордочкам и загните. Зубочисткой нарисуйте рот на кружке мордочки. Еще один "
                             "вариант печенья-мордочек можно сделать с помощью вырубки 'сердце'. Белое сердце - "
                             "мордочка, шоколадное пополам - ушки.", 2)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(6, "Выпекайте печенье-мордашки в разогретой до 200 °С духовке в течение 15 минут. Остудите "
                             "полностью. Приятного аппетита! Счастливого Нового года!", 2)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

dish = Dish("Рождественский кекс – это обязательное блюдо на Рождество на "
            "западе. Эта традиция дошла и до нас. Кекс получается невероятно "
            "вкусным благодаря цитрусам, специям и рождественскому волшебству.", "Кекс рождественский с мандаринами",
            7, TypesOfDish.SWEET_FOOD_AND_DRINKS)
db.session.add(dish)
db.session.flush()
db.session.commit()

recipe = Recipe("/static/img/keks_rojdestvenskii_s_mandarinami.jpg", "https://povar.ru/recipes"
                                                                     "/keks_rojdestvenskii_s_mandarinami-52483.html",
                "30 мин.", "2 ч.", 3)
db.session.add(recipe)
db.session.flush()
db.session.commit()

ingredient = Ingredient(150, "Сливочное масло", UnitsOfMeasurement.GRAM)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(125, "Сахар", UnitsOfMeasurement.GRAM)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(125, "Мука", UnitsOfMeasurement.GRAM)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(3, "Яйца", UnitsOfMeasurement.SHTUKI)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(1, "Разрыхлитель", UnitsOfMeasurement.TEA_SPOON)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(2, "Мандарины", UnitsOfMeasurement.SHTUKI)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(150, "Сухофрукты", UnitsOfMeasurement.GRAM)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(2, "Апельсиновый ликер", UnitsOfMeasurement.TABLE_SPOON)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(20, "Сливочное масло", UnitsOfMeasurement.GRAM)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(1, "Сахар", UnitsOfMeasurement.TEA_SPOON)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(1, "Мелкий сахар", UnitsOfMeasurement.TABLE_SPOON)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(1, "Яичный белок", UnitsOfMeasurement.SHTUKI)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(1, "Мандарины", UnitsOfMeasurement.SHTUKI)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(1, "Лимон", UnitsOfMeasurement.SHTUKI)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(1, "Веточка розмарина", UnitsOfMeasurement.SHTUKI)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

ingredient = Ingredient(1, "Сахарная пудра", UnitsOfMeasurement.TABLE_SPOON)
dish.Ingredients.append(ingredient)
db.session.add(ingredient)
db.session.flush()
db.session.commit()

implement = Implement("Миксер")
recipe.Implements.append(implement)
db.session.add(implement)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(1, "Очистите мандарины, выложите дольки на 1 час, чтобы пленочка немного подсохла.", 3)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(2, "Сухофрукты залейте апельсиновым ликером на 30 минут.", 3)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(3, "Размягченное сливочное масло взбейте с сахаром в пышную массу с помощью миксера.", 3)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(4, "Далее по одному вбивайте яйца, не останавливая работу миксера.", 3)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(5, "Просейте муку вместе с разрыхлителем и аккуратно взбивайте на небольшой скорости.", 3)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(6, "На разогретую сковороду выложите 20 грамм сливочного масла. Добавьте 1 ч.ложку сахара, "
                             "а затем выложите дольки мандарина и обжаривайте с каждой стороны по 2 минуты.", 3)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(7, "На эту же сковороду отправьте сухофрукты в ликере. Прогревайте, пока не испарится "
                             "алкоголь. Когда они остынут - отправьте их в тесто и аккуратно перемешайте.", 3)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(8, "Форму для выпечки смажьте маслом и присыпьте мукой. Выложите тесто, перекладывая его "
                             "карамелизированными мандаринами. Выпекайте 1 час в духовке, разогретой до 180 "
                             "градусов.", 3)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()

step_of_cook = StepOfCook(9, "Когда кекс остынет, украсьте его взбитым белком, присыпьте сахарной пудрой. Выложите "
                             "дольки мандарина и лимонную цедру. Розмарин заменит елочные ветки.", 3)
db.session.add(step_of_cook)
db.session.flush()
db.session.commit()
