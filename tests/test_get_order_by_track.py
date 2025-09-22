import pytest
import allure
from api.order_api import OrderApi
from data.test_data import TestData

# Создаем заказ
@allure.feature("Get Order by Track API")
class TestGetOrderByTrack:
    @pytest.fixture(autouse=True)
    def setup(self):

        order_data = TestData.get_order_data()
        create_response = OrderApi.create_order(order_data)
        self.track_id = create_response.json()["track"]
        
        yield
        
        OrderApi.cancel_order(self.track_id)
 # Тест успешного получения заказа по треку  
    @allure.title("Test successful get order by track")
    def test_get_order_by_track_success(self):
        response = OrderApi.get_order_by_track(self.track_id)
        
        assert response.status_code == 200
        assert "order" in response.json()
        assert response.json()["order"]["track"] == self.track_id
 # Тест получения заказа без номера трека   
    @allure.title("Test get order without track number")
    def test_get_order_without_track(self):
        response = OrderApi.get_order_by_track("")
        
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json()["message"]
 #Тест получения заказа с несуществующим треком  
    @allure.title("Test get order with non-existent track")
    def test_get_order_nonexistent_track(self):
        response = OrderApi.get_order_by_track("999999999")
        
        assert response.status_code == 404
        assert "Заказ не найден" in response.json()["message"]
#Тест получения заказа с невалидным треком    
    @allure.title("Test get order with invalid track")
    def test_get_order_invalid_track(self):
        response = OrderApi.get_order_by_track("invalid_track")
        
        assert response.status_code == 400