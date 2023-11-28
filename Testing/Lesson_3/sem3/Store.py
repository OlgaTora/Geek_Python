from Testing.Lesson_3.sem3.Cart import Cart
from Testing.Lesson_3.sem3.Product import Product


class Store:

    def __init__(self):
        self.inventory = []

    def add_product2inventory(self, product: Product):
        self.inventory.append(product)

    def get_inventory(self) -> list[Product]:
        return self.inventory

    def remove_product_from_inventory(self, product: Product):
        self.inventory.remove(product)

    def find_product_by_name(self, name: str) -> Product | None:
        for product in self.inventory:
            if product.get_name() == name:
                return product
        return None

    @staticmethod
    def create_cart() -> Cart:
        return Cart()
