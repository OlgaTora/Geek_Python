import unittest

from Testing.Lesson_3.sem3.Cart import Cart
from Testing.Lesson_3.sem3.Product import Product


class CartTest(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.product1 = Product("Apple", 999, 3)
        self.product2 = Product("Banana", 999.55, 3)

    def tearDown(self):
        self.cart = None

    def test_add_product(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.assertEqual(2, len(self.cart.get_products()))

    def test_remove_product(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.remove_product(self.product1)
        self.cart.remove_product(self.product2)
        self.assertEqual(0, len(self.cart.get_products()))

    def test_calculate_total_price(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        total_sum: float = self.cart.calculate_total_price()
        self.assertAlmostEqual(5995.65, total_sum)
