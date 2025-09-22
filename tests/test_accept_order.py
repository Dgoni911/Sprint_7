import pytest
import allure
from api.order_api import OrderApi
from data.expected_responses import ExpectedResponses
from data.test_data import TestData


@allure.feature("Accept Order API")
@allure.epic("Order Management")
class TestAcceptOrder:
#Тест успешного принятия заказа курьером    
    @allure.title("Успешное принятие заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_accept_order_success(self, setup_courier_and_order):
        with allure.step("Принять заказ валидным курьером"):
            response = OrderApi.accept_order(
                setup_courier_and_order["order_id"], 
                setup_courier_and_order["courier_id"]
            )
        
        with allure.step("Проверить код ответа и тело"):
            assert response.status_code == ExpectedResponses.SUCCESS_ACCEPT["code"]
            assert response.json() == ExpectedResponses.SUCCESS_ACCEPT["body"]
 #Тест принятия заказа без указания ID курьера   
    @allure.title("Принятие заказа без ID курьера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_accept_order_without_courier_id(self, setup_courier_and_order):
        with allure.step("Попытаться принять заказ без ID курьера"):
            response = OrderApi.accept_order(
                setup_courier_and_order["order_id"], 
                ""
            )
        
        with allure.step("Проверить ошибку недостатка данных"):
            assert response.status_code == ExpectedResponses.NOT_ENOUGH_DATA["code"]
            assert ExpectedResponses.NOT_ENOUGH_DATA["message"] in response.json()["message"]
#Тест принятия заказа с невалидным ID курьера    
    @allure.title("Принятие заказа с невалидным ID курьера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_accept_order_invalid_courier_id(self, setup_courier_and_order):
        with allure.step("Попытаться принять заказ с невалидным ID курьера"):
            response = OrderApi.accept_order(
                setup_courier_and_order["order_id"], 
                "invalid_id"
            )
        
        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 400
 #Тест принятия заказа без указания ID заказа   
    @allure.title("Принятие заказа без ID заказа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_accept_order_without_order_id(self, setup_courier_and_order):
        with allure.step("Попытаться принять заказ без ID заказа"):
            response = OrderApi.accept_order(
                "", 
                setup_courier_and_order["courier_id"]
            )
        
        with allure.step("Проверить ошибку недостатка данных"):
            assert response.status_code == ExpectedResponses.NOT_ENOUGH_DATA["code"]
            assert ExpectedResponses.NOT_ENOUGH_DATA["message"] in response.json()["message"]
 #Тест принятия заказа с несуществующим ID заказа  
    @allure.title("Принятие заказа с несуществующим ID заказа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_accept_order_invalid_order_id(self, setup_courier_and_order):
        with allure.step("Попытаться принять несуществующий заказ"):
            response = OrderApi.accept_order(
                "9999999999", 
                setup_courier_and_order["courier_id"]
            )
        
        with allure.step("Проверить ошибку ненайденного заказа"):
            assert response.status_code == ExpectedResponses.ORDER_NOT_EXIST["code"]
            assert ExpectedResponses.ORDER_NOT_EXIST["message"] in response.json()["message"]

#Тест принятия заказа с различными невалидными ID курьеров
    @allure.title("Принятие заказа с различными невалидными ID курьеров")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("invalid_courier_id", TestData.get_invalid_courier_ids())
    def test_accept_order_various_invalid_courier_ids(self, setup_courier_and_order, invalid_courier_id):
        with allure.step(f"Попытаться принять заказ с невалидным ID курьера: {invalid_courier_id}"):
            response = OrderApi.accept_order(
                setup_courier_and_order["order_id"], 
                invalid_courier_id
            )
        
        with allure.step("Проверить что запрос завершился ошибкой"):
            assert response.status_code != 200    