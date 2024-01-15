from Testing.Lesson_3.sem3.Product import Product


class Cart:

    def __init__(self):
        self.products = []

    def get_products(self) -> list[Product]:
        return self.products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def calculate_total_price(self) -> float:
        total_price: float = 0.0
        for product in self.products:
            total_price += product.get_price() * product.get_quantity()
        return total_price
