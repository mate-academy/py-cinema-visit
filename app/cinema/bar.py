from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        product = customer.food
        print(f"Cinema bar sold {product} to {customer.name}.")
