from __future__ import annotations
from app.people import customer


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
