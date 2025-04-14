class CinemaBar:
    @staticmethod
    def sell_product(customer: list, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")


class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food
