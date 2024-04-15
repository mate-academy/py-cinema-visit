from typing import List

from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: List[Customer], product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
