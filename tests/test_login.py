import pytest
import allure
from api.courier_api import CourierApi
from helpers.courier_helper import register_new_courier_and_return_login_password, generate_random_string

#Тест успешного логина курьера
@allure.feature("Login API")
class TestLogin:
    @allure.title("Test successful courier login")
    def test_login_success(self):
        courier_data = register_new_courier_and_return_login_password()
        login, password, _ = courier_data
        
        response = CourierApi.login_courier(login, password)
        
        assert response.status_code == 200
        assert "id" in response.json()
 #Тест логина с неправильным паролем   
    @allure.title("Test login with wrong password")
    def test_login_wrong_password(self):
        courier_data = register_new_courier_and_return_login_password()
        login, _, _ = courier_data
        
        response = CourierApi.login_courier(login, "wrong_password")
        
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json()["message"]
 # Тест логина несуществующего пользователя  
    @allure.title("Test login with non-existent user")
    def test_login_nonexistent_user(self):
        response = CourierApi.login_courier("nonexistent", "password")
        
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json()["message"]
 # Тест логина без обязательного поля  
    @allure.title("Test login without required field")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_field(self, missing_field):
        data = {"login": "test", "password": "test"}
        data.pop(missing_field)
        
        response = CourierApi.login_courier(**data)
        
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json()["message"]