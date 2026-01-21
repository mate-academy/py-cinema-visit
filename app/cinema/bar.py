from app.people.customer import Customer

from typing import Any


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str) -> Any:
        print(f"Cinema bar sold {product} to {customer.name}.")
