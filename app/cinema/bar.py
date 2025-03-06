class CinemaBar:

    @staticmethod
    def sell_product(customer: "Customer", product: str) -> None:
        print(f"Cinema bar sold {product} to {customer}.")


class Customer:

    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def __str__(self) -> str:
        return self.name

    def watch_movie(self) -> None:
        print(f"Customer {self.name} is watching a movie")


cb = CinemaBar()
customer = Customer("Bob", "popcorn")
cb.sell_product(customer=customer, product=customer.food)
