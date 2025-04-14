class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")


class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food


cb = CinemaBar()
customer = Customer("Bob", "popcorn")
cb.sell_product(customer=customer, product=customer.food)
# Cinema bar sold popcorn to Bob.
