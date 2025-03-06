class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str) -> str:
        print(f"Cinema bar sold {product} to {customer.name}.")
