import pytest
import allure
from api.courier_api import CourierApi
from helpers.courier_helper import register_new_courier_and_return_login_password

#Тест успешного удаления курьера
@allure.feature("Delete Courier API")
class TestDeleteCourier:
    @allure.title("Test successful courier deletion")
    def test_delete_courier_success(self):
        courier_data = register_new_courier_and_return_login_password()
        login, password, _ = courier_data
        
        login_response = CourierApi.login_courier(login, password)
        courier_id = login_response.json()["id"]
        
        delete_response = CourierApi.delete_courier(courier_id)
        
        assert delete_response.status_code == 200
        assert delete_response.json() == {"ok": True}
#Тест удаления курьера без ID    
    @allure.title("Test delete courier without id")
    def test_delete_courier_without_id(self):
        response = CourierApi.delete_courier("")
        
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json()["message"]
 #Тест удаления несуществующего курьера   
    @allure.title("Test delete non-existent courier")
    def test_delete_nonexistent_courier(self):
        response = CourierApi.delete_courier("9999999999")
        
        assert response.status_code == 404
        assert "Курьера с таким id нет" in response.json()["message"]
# Тест удаления курьера с невалидным ID   
    @allure.title("Test delete courier with invalid id")
    def test_delete_courier_invalid_id(self):
        response = CourierApi.delete_courier("invalid_id")
        
        assert response.status_code == 400