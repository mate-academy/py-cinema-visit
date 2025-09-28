from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(costumer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {costumer.name}")
