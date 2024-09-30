import pytest
from praktikum.bun import Bun


class TestBun:
    def test_get_name_positive(self):
        # Создаем объект класса и устанавливаем параметры
        new_bun = Bun('Флюоресцентная булка R2-D3', 988.4)
        # Проверяем, что полученное имя соответствует установленному в параметре класса имени
        assert new_bun.get_name() == 'Флюоресцентная булка R2-D3'

    def test_get_price_positive(self):
        # Создаем объект класса и устанавливаем параметры
        new_bun = Bun('Флюоресцентная булка R2-D3', 988.4)
        # Проверяем, что полученная цена соответствует установленной в параметре класса цене
        assert new_bun.get_price() == 988.4