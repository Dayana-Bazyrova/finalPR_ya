#Базырова Даяна, 9-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import requests

def truck_order_code_200():
    response = sender_stand_request.truck_order()
    assert response.truck_order_code_200 == 200


def test_order():
    truck_order_code_200
