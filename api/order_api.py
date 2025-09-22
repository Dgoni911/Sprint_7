import requests
import allure
from config import URLs


class OrderApi:
    
    @staticmethod
    def create_order(order_data):
        return requests.post(URLs.ORDERS, json=order_data)
    
    @staticmethod
    def get_orders_list():
        return requests.get(URLs.ORDERS)
    
    @staticmethod
    def get_order_by_track(track_id):
        return requests.get(f"{URLs.ORDERS}/track", params={"t": track_id})
    
    @staticmethod
    def accept_order(order_id, courier_id):
        return requests.put(f"{URLs.ORDERS}/accept/{order_id}", params={"courierId": courier_id})
    
    @staticmethod
    def cancel_order(track_id):
        return requests.put(f"{URLs.ORDERS}/cancel", params={"track": track_id})
    @staticmethod
    @allure.step("Создать заказ")
    def create_order(order_data):
        return requests.post(URLs.ORDERS, json=order_data)
    
    @staticmethod
    @allure.step("Получить список заказов")
    def get_orders_list():
        return requests.get(URLs.ORDERS)
    
    @staticmethod
    @allure.step("Получить заказ по треку {track_id}")
    def get_order_by_track(track_id):
        return requests.get(f"{URLs.ORDERS}/track", params={"t": track_id})
    
    @staticmethod
    @allure.step("Принять заказ {order_id} курьером {courier_id}")
    def accept_order(order_id, courier_id):
        return requests.put(f"{URLs.ORDERS}/accept/{order_id}", params={"courierId": courier_id})
    
    @staticmethod
    @allure.step("Отменить заказ {track_id}")
    def cancel_order(track_id):
        return requests.put(f"{URLs.ORDERS}/cancel", params={"track": track_id})