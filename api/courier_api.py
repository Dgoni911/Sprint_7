import requests
import allure
from config import URLs


class CourierApi:
    
    @staticmethod
    @allure.step("Создать курьера: {login}")
    def create_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(URLs.COURIER, data=payload)
    
    @staticmethod
    @allure.step("Логин курьера: {login}")
    def login_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(URLs.COURIER_LOGIN, data=payload)
    
    @staticmethod
    @allure.step("Удалить курьера {courier_id}")
    def delete_courier(courier_id):
        return requests.delete(f"{URLs.COURIER}/{courier_id}")