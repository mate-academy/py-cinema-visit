from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: Customer) -> str:
        return f"Cinema bar sold {product} ot {customer.name}."
