import unittest

from Testing.Lesson_3.sem3.Cart import Cart
from Testing.Lesson_3.sem3.Product import Product
from Testing.Lesson_3.sem3.Store import Store


class StoreTest(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.product1 = Product("Apple", 999, 3)
        self.product2 = Product("Banana", 999.55, 3)

    def tearDown(self):
        self.store = None
        self.product1 = None
        self.product2 = None

    def test_add_product2inventory(self):
        """Проверка сохранения продуктов в Store.inventory"""
        self.store.add_product2inventory(self.product1)
        self.store.add_product2inventory(self.product2)
        self.assertEqual(2, len(self.store.get_inventory()))

    def test_remove_product_from_inventory(self):
        self.store.add_product2inventory(self.product1)
        self.store.remove_product_from_inventory(self.product1)
        self.assertEqual(0, len(self.store.get_inventory()))

    def test_find_product_by_name(self):
        self.store.add_product2inventory(self.product1)
        find_product: Product = self.store.find_product_by_name('Apple')
        self.assertEqual('Apple', find_product.get_name())

    def test_create_cart(self):
        cart: Cart = self.store.create_cart()
        self.assertIsNotNone(cart)
