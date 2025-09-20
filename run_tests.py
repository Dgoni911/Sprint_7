import pytest
import os

if __name__ == "__main__":
    # Создаем директорию для результатов Allure
    os.makedirs("allure-results", exist_ok=True)
    
    # Запускаем тесты с генерацией Allure отчета
    pytest.main([
        "-v",
        "--alluredir=allure-results",
        "tests/"
    ])