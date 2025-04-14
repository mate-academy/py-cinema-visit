from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:
    """This class describes work of cinema bar"""

    @staticmethod
    def sell_product(customer: Customer, product: str) -> str:
        print(f"Cinema bar sold {product} to {customer.name}.")
