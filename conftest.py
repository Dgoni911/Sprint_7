import pytest
import allure
from api.courier_api import CourierApi
from api.order_api import OrderApi
from helpers.courier_helper import register_new_courier_and_return_login_password
from data.test_data import TestData

#Для создания курьера и заказа
@pytest.fixture
def setup_courier_and_order():
# Создаем курьера
    courier_data = register_new_courier_and_return_login_password()
    login, password, _ = courier_data
    login_response = CourierApi.login_courier(login, password)
    courier_id = login_response.json()["id"]
    
# Создаем заказ
    order_data = TestData.get_order_data()
    create_response = OrderApi.create_order(order_data)
    track_id = create_response.json()["track"]
    
    # Получаем ID заказа
    track_response = OrderApi.get_order_by_track(track_id)
    order_id = track_response.json()["order"]["id"]
    
# Возвращаем все данные
    yield {
        "courier_id": courier_id,
        "track_id": track_id,
        "order_id": order_id,
        "login": login,
        "password": password
    }
# Очистка после теста
    OrderApi.cancel_order(track_id)
    CourierApi.delete_courier(courier_id)

#Фикстура для создания зарегистрированного курьера
@pytest.fixture
def registered_courier():
    from helpers.courier_helper import register_new_courier_and_return_login_password
    courier_data = register_new_courier_and_return_login_password()
    yield courier_data  # возвращаем данные курьера
    
# Удаляем курьера после теста
    login, password, _ = courier_data
    login_response = CourierApi.login_courier(login, password)
    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        CourierApi.delete_courier(courier_id)


