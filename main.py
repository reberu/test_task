# Задание:
# В Якутске 8 марта. Люди поздравляют друг друга и заказывают подарки, цветы и сладости.
# Задача:
# Написать алгоритм распределения заказов между курьерами, чтобы был приоритет в скорости доставки посылки клиентам.
# Входные параметры:
# Список заказов
#   Параметры заказа:
#       Гео-координаты точки А (Откуда), Гео-координаты точки Б (Куда), Стоимость заказа
# Список курьеров
#   Параметры курьера:
#       Гео-координаты курьера

import math


def haversine(coord1: tuple, coord2: tuple) -> float:
    """ Вычисление расстояния между двумя координатами
    Принимает на вход 2 кортежа, состоящих из координат в градусах
    :param coord1: первая координата; кортеж (широта, долгота) в десятичных градусах
    :param coord2: вторая координата; кортеж (широта, долгота) в десятичных градусах
    :return: расстояние между двумя координатами в километрах в формате float
    """
    R = 6371  # Радиус Земли в километрах
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


def assign_orders(order_list: list, couriers_list: list) -> dict:
    """ Назначение курьеров для каждого заказа
    Принимает на вход 2 списка.
    :param order_list: список заказов
    :param couriers_list: список курьеров
    :return: назначенные заказы в формате dict
    """
    assignments = {}
    for o in order_list:
        order_location = o['from']
        courier = min(couriers_list, key=lambda x: haversine(x['location'], order_location))
        assignments[courier['id']] = o
    return assignments
