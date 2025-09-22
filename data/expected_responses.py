class ExpectedResponses:
    
    NOT_ENOUGH_DATA = {
        "code": 400,
        "message": "Недостаточно данных для входа"
    }
    
    # Курьер
    COURIER_ALREADY_EXISTS = {
        "code": 409,
        "message": "Этот логин уже используется"
    }
    
    COURIER_NOT_FOUND = {
        "code": 404,
        "message": "Учетная запись не найдена"
    }
    
    # Успешные ответы
    SUCCESS_CREATE = {
        "code": 201,
        "body": {"ok": True}
    }
    
    SUCCESS_DELETE = {
        "code": 200,
        "body": {"ok": True}
    }
