from __future__ import annotations
from app.people import customer as buyer


class CinemaBar:
    @staticmethod
    def sell_product(
            product: str,
            customer: buyer.Customer
    ) -> None:
        print(f"Cinema bar sold {product} to {customer}.")
