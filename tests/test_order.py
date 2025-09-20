import pytest
import allure
from api.order_api import OrderApi
from data.test_data import TestData

#Тест создания заказа с разными цветами
@allure.feature("Order API")
class TestOrder:
    @allure.title("Test create order with different colors")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order_with_colors(self, color):
        order_data = TestData.get_order_data(color)
        
        response = OrderApi.create_order(order_data)
        
        assert response.status_code == 201
        assert "track" in response.json()
 #Тест получения списка заказов   
    @allure.title("Test get orders list")
    def test_get_orders_list(self):
        response = OrderApi.get_orders_list()
        
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)