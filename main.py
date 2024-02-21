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
    Принимает на вход 2 кортежа, состоящих из координат в десятичных градусах
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
    while order_list:
        min_total_distance = float('inf')
        selected_courier = None
        selected_order = None
        for courier in couriers_list:
            if not order_list:
                break
            order = min(order_list,
                        key=lambda x: haversine(courier['location'], x['from']) + haversine(x['from'], x['to']))
            total_distance = haversine(courier['location'], order['from']) + haversine(order['from'], order['to'])
            if total_distance < min_total_distance:
                min_total_distance = total_distance
                selected_courier = courier
                selected_order = order
        if selected_courier:
            assignments[selected_courier['location']] = selected_order
            order_list.remove(selected_order)
    return assignments


if __name__ == '__main__':
    # Пример входных данных
    orders = [
        {'from': (1, 2), 'to': (5, 5), 'cost': 50},
        {'from': (2, 3), 'to': (6, 4), 'cost': 70},
        {'from': (3, 4), 'to': (8, 9), 'cost': 60},
    ]

    couriers = [
        {'location': (2, 3)},
        {'location': (6, 7)},
        {'location': (4, 5)},
        {'location': (1, 2)},
    ]

    assigned_orders = assign_orders(orders, couriers)

    for courier, order in assigned_orders.items():
        print(f"Курьер {courier} доставит заказ {order}")
