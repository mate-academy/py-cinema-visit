"""
bar.py

This module describes the work of a cinema bar.
"""

from app.people.customer import Customer


class CinemaBar:
    """Represents a cinema bar that sells products to customers."""

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """
        Sell a product to a customer and display information about the sale.

        :param product: str, the name of the product the customer wants to buy.
        :param customer: Customer, an instance representing the customer.
        """
        print(f"Cinema bar sold {product} to {customer.name}.")
