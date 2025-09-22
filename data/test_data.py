class TestData:
    @staticmethod
    def get_order_data(color=None):
        base_data = {
            "firstName": "Евгений",
            "lastName": "Косач",
            "address": "Ленинградский проспект, 53",
            "metroStation": 10,
            "phone": "+79181234564",
            "rentTime": 6,
            "deliveryDate": "2024-09-30",
            "comment": "Тестовый заказ"
        }
        
        if color:
            if isinstance(color, list):
                base_data["color"] = color
            else:
                base_data["color"] = [color]
        
        return base_data
    
    @staticmethod
    def get_invalid_courier_ids():
        return ["", "invalid_id", "9999999999", None]
    
    @staticmethod
    def get_invalid_order_ids():
        return ["", "invalid_order_id", "9999999999", None]