from __future__ import annotations
from app.people.customer import Customer
"""
that module describes work of cinema bar
"""


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        if customer and isinstance(customer, Customer) and product:
            print(f"Cinema bar sold {product} to {customer.name}.")
