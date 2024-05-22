import pytest
import allure


@allure.feature('Создание и выгрузка заказов')
class TestOrder:
    @allure.title('Можно указать один из цветов — BLACK или GREY, ответ содержит "track"')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],])
    def test_create_order_successful(self, color, create_order):
        create_order.payload["color"] = color
        response = create_order.post_create_order(data=create_order.payload)
        assert "track" in response

    @allure.title('Можно не указывать цвет, ответ содержит "track"')
    def test_order_no_color(self, create_order):
        response = create_order.post_create_order(data=create_order.payload)
        assert "track" in response

    @allure.title('Тело ответа возвращается список заказов')
    def test_get_order_list(self, create_order):
        response = create_order.list_of_orders()
        assert "orders" in response
