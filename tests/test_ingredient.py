import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:
    def test_get_price(self):
        # Создаем объект класса и добавляем значения параметров
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Тестовый пикантный соус', 205.3)
        # Проверяем, что полученная цена соответствует установленной в параметрах
        assert new_ingredient.get_price() == 205.3

    def test_get_name(self):
        # Создаем объект класса и добавляем значения параметров
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Тестовый пикантный соус', 205.3)
        # Проверяем, что полученное название соответствует установленному в параметрах
        assert new_ingredient.get_name() == 'Тестовый пикантный соус'

    @pytest.mark.parametrize('ingredient_type, exp_type', ([INGREDIENT_TYPE_SAUCE, 'SAUCE'], [INGREDIENT_TYPE_FILLING, 'FILLING']))
    def test_get_type(self, ingredient_type, exp_type):
        # Создаем объект класса и добавляем значения параметров
        ingredient = Ingredient(ingredient_type, 'Пикантная начинка', 205.3)
        # Проверяем, что полученный тип соответствует установленному ожидаемому типу ингредиента в параметризации
        assert ingredient.get_type() == exp_type
