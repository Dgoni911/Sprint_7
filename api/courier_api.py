import requests


class CourierApi:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"
    
    @staticmethod
    def create_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(CourierApi.BASE_URL, data=payload)
    
    @staticmethod
    def login_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(f"{CourierApi.BASE_URL}/login", data=payload)
    
    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{CourierApi.BASE_URL}/{courier_id}")