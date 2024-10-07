import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns(self):
        # Создаем объект класса
        burger = Burger()
        # Создаем мок
        mock_bun = Mock()
        # Присваиваем моку параметры
        mock_bun.get_name.return_value = 'Замокированная супербулка'
        mock_bun.get_price.return_value = 800.5
        # Вызываем функцию и устанавливаем значение для булки
        burger.set_buns(mock_bun)
        # Проверяем, что булка внутри класса соответствует моку
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        # Создаем объект класса
        burger = Burger()
        # Создаем мок
        mock_ingredient = Mock()
        # Присваиваем моку параметры
        mock_ingredient.type = 'SAUCE'
        mock_ingredient.name = 'Мокированная пикантная начинка'
        mock_ingredient.price = 205.3
        # Вызываем функцию и передаем мокированный элемент
        burger.add_ingredient(mock_ingredient)
        # Проверяем, что добавленный ингредиент внутри класса соответствует моку
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self):
        # Создаем объект класса
        burger = Burger()
        # Создаем мок
        mock_ingredient = Mock()
        # Присваиваем моку параметры
        mock_ingredient.type = 'SAUCE'
        mock_ingredient.name = 'Мокированная пикантная начинка'
        mock_ingredient.price = 205.3
        # Вызываем функцию и передаем мокированный элемент
        burger.add_ingredient(mock_ingredient)
        # Удаляем ингредиент
        burger.remove_ingredient(0)
        # Проверяем, что добавленный ингредиент внутри класса был удален
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self):
        # Создаем объект класса
        burger = Burger()
        # Создаем моки
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        # Устанавливаем ингредиенты
        burger.ingredients = [mock_ingredient2, mock_ingredient1]
        # Передвигаем ингредиент с mock_ingredient2 на второе место
        burger.move_ingredient(0, 1)
        # Проверяем, что ингредиенты располагаются в нужном нам порядке
        assert burger.ingredients == [mock_ingredient1, mock_ingredient2]

    def test_get_price(self):
        # Создаем объект класса
        burger = Burger()
        # Создаем моки
        mock_bun = Mock()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        # Устанавливаем значения цен для моков
        mock_bun.get_price.return_value = 111.1
        mock_ingredient1.get_price.return_value = 205.3
        mock_ingredient2.get_price.return_value = 89.3
        # Устанавливаем значение булки
        burger.bun = mock_bun
        # Устанавливаем значения ингредиентов
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        # Проверяем, что сумма цен ингредиентов, а также двух булок - корректная
        assert burger.get_price() == 516.8

    def test_get_receipt(self):
        # Создаем объект класса
        burger = Burger()
        # Создаем моки
        mock_bun = Mock()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_burger = Mock()
        # Устанавливаем значения параметров для моков
        mock_bun.get_name.return_value = 'Мокированная булочка'
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient1.get_name.return_value = 'Мокированная начинка'
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient2.get_name.return_value = 'Мокированный соус'
        mock_burger.get_price.return_value = 516.8
        # Устанавливаем значение булки
        burger.bun = mock_bun
        # Устанавливаем значения ингредиентов
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        # Устанавливаем значение цены
        burger.get_price = mock_burger.get_price
        # Создаем ожидаемый строковый рецепт бургера
        expected_receipt = '(==== Мокированная булочка ====)\n' \
                           '= filling Мокированная начинка =\n' \
                           '= sauce Мокированный соус =\n' \
                           '(==== Мокированная булочка ====)\n' \
                           '\nPrice: 516.8'
        # Проверяем, что рецепт соответствует ожидаемому
        assert burger.get_receipt() == expected_receipt
