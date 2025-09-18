class CinemaBar:
    def __init__(self):
        self.menu = {}

    def get_price(self, item: str):
        return self.menu.get(item)

    def buy(self, item: str, qty: int):
        price = self.get_price(item)
        if price is None:
            return None
        return price * max(qty, 0)

    def sell_product(self, customer, product: str) -> None:
        # Texto exato que o teste espera:
        print(f"Cinema bar sold {product} to {customer.name}.")
