class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")


customer = Customer("Bob", "popcorn")

CinemaBar.sell_product(product=customer.food, customer=customer)
