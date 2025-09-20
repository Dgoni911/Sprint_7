import pytest
import allure
from api.order_api import OrderApi
from api.courier_api import CourierApi
from data.test_data import TestData
from helpers.courier_helper import register_new_courier_and_return_login_password, generate_random_string

#Создаем курьера,заказ,Получаем ID заказа
@allure.feature("Accept Order API")
class TestAcceptOrder:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.courier_data = register_new_courier_and_return_login_password()
        login, password, _ = self.courier_data
        login_response = CourierApi.login_courier(login, password)
        self.courier_id = login_response.json()["id"]
        
        order_data = TestData.get_order_data()
        create_response = OrderApi.create_order(order_data)
        self.track_id = create_response.json()["track"]
        
        track_response = OrderApi.get_order_by_track(self.track_id)
        self.order_id = track_response.json()["order"]["id"]
        
        yield
        
        OrderApi.cancel_order(self.track_id)
        CourierApi.delete_courier(self.courier_id)
# Тест успешного принятия заказа   
    @allure.title("Test successful order acceptance")
    def test_accept_order_success(self):
        response = OrderApi.accept_order(self.order_id, self.courier_id)
        
        assert response.status_code == 200
        assert response.json() == {"ok": True}
 # Тест принятия заказа без ID курьера  
    @allure.title("Test accept order without courier id")
    def test_accept_order_without_courier_id(self):
        response = OrderApi.accept_order(self.order_id, "")
        
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json()["message"]
# Тест принятия заказа с невалидным ID курьера   
    @allure.title("Test accept order with invalid courier id")
    def test_accept_order_invalid_courier_id(self):
        response = OrderApi.accept_order(self.order_id, "invalid_id")
        
        assert response.status_code == 400
 # Тест принятия заказа без ID заказа  
    @allure.title("Test accept order without order id")
    def test_accept_order_without_order_id(self):
        response = OrderApi.accept_order("", self.courier_id)
        
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json()["message"]
# Тест принятия заказа с невалидным ID заказа   
    @allure.title("Test accept order with invalid order id")
    def test_accept_order_invalid_order_id(self):
        response = OrderApi.accept_order("9999999999", self.courier_id)
        
        assert response.status_code == 404
        assert "Заказа с таким id не существует" in response.json()["message"]