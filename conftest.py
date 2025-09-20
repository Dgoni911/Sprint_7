import pytest
import allure
from helpers.courier_helper import register_new_courier_and_return_login_password, delete_courier_by_login
from api.order_api import OrderApi

#Для создания и удаления курьера
@pytest.fixture
def create_and_delete_courier():
    courier_data = register_new_courier_and_return_login_password()
    yield courier_data  
    login, password, _ = courier_data
    delete_courier_by_login(login, password)

#Для создания и отмены заказа
@pytest.fixture
def create_and_cancel_order():
    from data.test_data import TestData
    order_data = TestData.get_order_data()
    create_response = OrderApi.create_order(order_data)
    track_id = create_response.json()["track"]
    yield track_id  
    OrderApi.cancel_order(track_id)