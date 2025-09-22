import pytest
import allure
from api.courier_api import CourierApi
from helpers.courier_helper import generate_random_string
from data.expected_responses import ExpectedResponses


@allure.feature("Courier API")
@allure.epic("Courier Management")
class TestCourier:
 #Тест успешного создания курьера   
    @allure.title("Успешное создание курьера")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_courier_success(self, courier_data):
        login, password, first_name = courier_data
        
        with allure.step("Создать нового курьера"):
            response = CourierApi.create_courier(login, password, first_name)
        
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}
        
        # Очистка после теста
        with allure.step("Удалить созданного курьера"):
            login_response = CourierApi.login_courier(login, password)
            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                CourierApi.delete_courier(courier_id)
#Тест создания дубликата курьера   
    @allure.title("Создание дубликата курьера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_duplicate_courier(self, registered_courier):
        login, password, first_name = registered_courier
        
        with allure.step("Попытаться создать курьера с существующим логином"):
            response = CourierApi.create_courier(login, password, first_name)
        
        with allure.step("Проверить ошибку конфликта"):
            assert response.status_code == 409
            assert "уже существует" in response.json()["message"]
 #Тест создания курьера без обязательного поля  
    @allure.title("Создание курьера без обязательного поля")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, courier_data, missing_field):
        login, password, first_name = courier_data
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        data.pop(missing_field)
        
        with allure.step(f"Создать курьера без поля {missing_field}"):
            response = CourierApi.create_courier(**data)
        
        with allure.step("Проверить ошибку недостатка данных"):
            assert response.status_code == ExpectedResponses.NOT_ENOUGH_DATA["code"]
            assert ExpectedResponses.NOT_ENOUGH_DATA["message"] in response.json()["message"]