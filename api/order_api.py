import requests


class OrderApi:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/orders"
    
    @staticmethod
    def create_order(order_data):
        return requests.post(OrderApi.BASE_URL, json=order_data)
    
    @staticmethod
    def get_orders_list():
        return requests.get(OrderApi.BASE_URL)
    
    @staticmethod
    def get_order_by_track(track_id):
        return requests.get(f"{OrderApi.BASE_URL}/track", params={"t": track_id})
    
    @staticmethod
    def accept_order(order_id, courier_id):
        return requests.put(f"{OrderApi.BASE_URL}/accept/{order_id}", params={"courierId": courier_id})
    
    @staticmethod
    def cancel_order(track_id):
        return requests.put(f"{OrderApi.BASE_URL}/cancel", params={"track": track_id})