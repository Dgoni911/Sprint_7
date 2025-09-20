import requests
import random
import string
from api.courier_api import CourierApi


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

#Регистрирует нового курьера и возвращает логин, пароль и имя
def register_new_courier_and_return_login_password():
    login_pass = []
    
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    
    return login_pass

#Удаляет курьера по логину и паролю
def delete_courier_by_login(login, password):
    login_response = CourierApi.login_courier(login, password)
    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        CourierApi.delete_courier(courier_id)