from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:
    def __init__(self) -> None:
        pass

    @staticmethod
    def sell_product(customer: CinemaBar, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")


if __name__ == "__main__":
    cb = CinemaBar()
    customer = Customer("Bob", "popcorn")
    cb.sell_product(customer=customer.name, product=customer.food)
