import unittest

from main import assign_orders


class TestNearestNeighbor(unittest.TestCase):
    def test_nearest_neighbor(self):
        c1 = (62.025989407890336, 129.73190770225227)  # Национальный художественный музей
        c2 = (62.029481822056006, 129.72959027366335)  # ТРК Туймаада
        dest1 = (62.034394734161665, 129.71822570629917)
        dest2 = (62.02924340678772, 129.73433793629852)
        orders = [
            {'id': 1, 'from': c1, 'to': dest1, 'cost': 250},
            {'id': 2, 'from': c2, 'to': dest2, 'cost': 200},
        ]

        cur1_loc = (62.02854738921128, 129.73254931857454)
        cur2_loc = (62.030550874809244, 129.76234239242137)
        cur3_loc = (62.040925954433554, 129.7287578401876)
        cur4_loc = (62.00975627297603, 129.7212625753115)
        cur5_loc = (62.026866363029974, 129.73459549840848)
        couriers = [
            {'id': 1, 'location': cur1_loc},
            {'id': 2, 'location': cur2_loc},
            {'id': 3, 'location': cur3_loc},
            {'id': 4, 'location': cur4_loc},
            {'id': 5, 'location': cur5_loc},
        ]

        assigned_orders = assign_orders(orders, couriers)

        self.assertEqual(len(assigned_orders), len(orders))  # Проверяем, что всем заказам назначены курьеры

        for courier in couriers:
            self.assertNotIn(courier['location'],
                             [order['to'] for order in orders])  # Проверяем, что каждый заказ был назначен


if __name__ == '__main__':
    unittest.main()
