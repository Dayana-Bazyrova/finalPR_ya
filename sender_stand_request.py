#Базырова Даяна, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import configuration
import requests



# cоздать заказ
def post_create_orders(body):
   return requests.post(configuration.URL_SERVER + configuration.CREATE_ORDERS,
                        json=body)

# Сохранить трек-номер заказа
def get_new_track():
    new_order = post_create_orders(data.order_body)
    track_number = new_order.json()['track']
    return track_number


#Получить заказ по трек номеру
def truck_order():
    track = get_new_track()
    return requests.get(configuration.URL_SERVER + configuration.GET_ORDERS + str(track))







