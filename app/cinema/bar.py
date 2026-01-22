from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer | str, product: str) -> None:
        if isinstance(customer, Customer):
            print(f"Cinema bar sold {product} to {customer.name}.")
        elif isinstance(customer, str):
            print(f"Cinema bar sold {product} to {customer}.")
