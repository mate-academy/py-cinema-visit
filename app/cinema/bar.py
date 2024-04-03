from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:
    def __init__(self) -> None:
        pass

    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
