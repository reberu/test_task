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


def calculate_distance(coord1: tuple, coord2: tuple) -> float:
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
    assignments: dict = {}

    # Назначаем каждому курьеру ближайший заказ
    for courier in couriers_list:
        min_distance = float('inf')
        closest_order = None
        for spare_order in order_list:
            distance = calculate_distance(courier['location'], spare_order['from'])
            if distance < min_distance:
                min_distance = distance
                closest_order = spare_order
        if closest_order:
            assignments[courier['id']] = [closest_order]
            order_list.remove(closest_order)  # Удаляем заказ из списка, чтобы он не был назначен другому курьеру

    # Добавляем дополнительные заказы для каждого курьера, если возможно
    while order_list:
        for cour_id, assignment in assignments.items():
            last_order = assignment[-1]  # Последний назначенный заказ
            closest_order = None
            min_distance = float('inf')
            for spare_order in order_list:
                # Проверяем расстояние от последней точки доставки курьера до точки получения заказа
                distance = calculate_distance(last_order['to'], spare_order['from'])
                if distance < min_distance:
                    # Проверяем, что ни один другой курьер не ближе к точке А следующего заказа
                    if all(calculate_distance(current_order[-1]['to'], spare_order['from']) >=
                           distance for current_order in assignments.values()):
                        min_distance = distance
                    else:
                        min_distance = min(calculate_distance(current_order[-1]['to'], spare_order['from'])
                                           for current_order in assignments.values())
                    closest_order = spare_order
            if closest_order:
                assignment.append(closest_order)  # Добавляем следующий заказ к текущему курьеру
                order_list.remove(closest_order)  # Удаляем заказ из списка, чтобы он не был назначен другому курьеру
            else:
                break  # Если не нашли подходящий заказ для добавления, завершаем цикл
    return assignments


if __name__ == '__main__':
    # Пример входных данных
    orders = [
        {'from': (1, 2), 'to': (5, 5), 'cost': 50},
        {'from': (2, 3), 'to': (6, 4), 'cost': 70},
        {'from': (3, 4), 'to': (8, 9), 'cost': 60},
        {'from': (5, 3), 'to': (2, 2), 'cost': 70},
        {'from': (4, 4), 'to': (1, 9), 'cost': 60},
    ]

    couriers = [
        {'location': (2, 3)},
        {'location': (6, 7)},
        {'location': (4, 5)},
        {'location': (1, 2)},
    ]
    # Для удобства работы назначим каждому курьеру идентификатор
    couriers = [{'id': idx, **courier} for idx, courier in enumerate(couriers, start=1)]

    assigned_orders = assign_orders(orders, couriers)

    for courier_id, orders in assigned_orders.items():
        print(f"Курьеру {courier_id} назначены заказы:")
        for order in orders:
            print(order)
        print()
