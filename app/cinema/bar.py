from __future__ import annotations
from typing import Any
from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(customer: Customer, product: str) -> Any:
        print(f"Cinema bar sold {product} to {customer.name}.")
