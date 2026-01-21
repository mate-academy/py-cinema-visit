from __future__ import annotations
from app.people.customer import Customer


class CinemaBar:
    """A class to represent a cinema bar."""

    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        """Sells a product to a customer.

        :param customer: The customer to sell the product to.
        :type customer: Customer
        :param product: The product to sell.
        :type product: str
        """
        print(f"Cinema bar sold {product} to {customer.name}.")
