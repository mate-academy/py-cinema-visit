from __future__ import annotations

from app.people.customer import Customer


class CinemaBar:
    """
    class that describes work of cinema bar.
    """

    @staticmethod
    def sell_product(customer: "Customer", product: str) -> None:
        """
        method sells a product to the customer
        and displays which product was sold and to whom.
        """

        print(f"Cinema bar sold {product} to {customer.name}.")
