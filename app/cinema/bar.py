from __future__ import annotations

from app.people import customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: customer.Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
