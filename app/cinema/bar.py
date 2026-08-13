from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")


if __name__ == "__main__":
    cb = CinemaBar()
    customer = Customer("Bob", "popcorn")
    CinemaBar.sell_product(product=customer.food, customer=customer)