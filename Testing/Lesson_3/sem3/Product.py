class Product:

    def __init__(self, name: str, price: float, quantity: int):
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity

    def set_name(self, name: str):
        self.name = name

    def set_price(self, price: float):
        self.price = price

    def set_quantity(self, quantity: int):
        self.quantity = quantity

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def get_quantity(self) -> int:
        return self.quantity
