import pytest
import allure
from api.courier_api import CourierApi
from helpers.courier_helper import register_new_courier_and_return_login_password, generate_random_string

#Тест создания курьера
@allure.feature("Courier API")
class TestCourier:
    @allure.title("Test successful courier creation")
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        
        response = CourierApi.create_courier(login, password, first_name)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
#Тест создания курьера второй раз    
    @allure.title("Test duplicate courier creation")
    def test_create_duplicate_courier(self):
        courier_data = register_new_courier_and_return_login_password()
        login, password, first_name = courier_data
        
        response = CourierApi.create_courier(login, password, first_name)
        
        assert response.status_code == 409
        assert "уже существует" in response.json()["message"]
 #Тест создания курьера без обязательного поля   
    @allure.title("Test courier creation without required field")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, missing_field):
        data = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        data.pop(missing_field)
        
        response = CourierApi.create_courier(**data)
        
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json()["message"]