from __future__ import annotations


class CinemaBar:
    @staticmethod
    def sell_product(customer: object, product: str):
        print(f"Cinema bar sold {product} to {customer.name}.")
