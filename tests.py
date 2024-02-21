import unittest

from main import assign_orders

c1 = (62.025989407890336, 129.73190770225227)
c2 = (62.029481822056006, 129.72959027366335)
dest1 = (62.034394734161665, 129.71822570629917)
dest2 = (62.02924340678772, 129.73433793629852)
orders = [
    {'from': c1, 'to': dest1, 'cost': 250},
    {'from': c2, 'to': dest2, 'cost': 200},
]

cur1_loc = (62.02854738921128, 129.73254931857454)
cur2_loc = (62.030550874809244, 129.76234239242137)
cur3_loc = (62.040925954433554, 129.7287578401876)
cur4_loc = (62.00975627297603, 129.7212625753115)
cur5_loc = (62.026866363029974, 129.73459549840848)
couriers = [
    {'location': cur1_loc},
    {'location': cur2_loc},
    {'location': cur3_loc},
    {'location': cur4_loc},
    {'location': cur5_loc},
]


class TestNearestCourier(unittest.TestCase):
    def test_orders_set(self):
        orders_len = len(orders)
        assigned_orders = assign_orders(orders, couriers)
        self.assertEqual(len(assigned_orders), orders_len)  # Проверяем, что всем заказам назначены курьеры

    def test_various_courier(self):
        assigned_orders = assign_orders(orders, couriers)
        assigned_couriers = set()
        for courier in assigned_orders.keys():
            assigned_couriers.add(courier)
        self.assertEqual(len(assigned_couriers), len(orders))  # Проверяем, что каждый заказ имеет своего курьера


if __name__ == '__main__':
    unittest.main()
