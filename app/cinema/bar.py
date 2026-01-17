from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(customer: Customer, product: Customer) -> None:
        """ Customer name and product """

        print(f"Cinema bar sold {product} to {customer.name}.")
