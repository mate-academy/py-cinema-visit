from __future__ import annotations


class CinemaBar:
    def __init__(self) -> None:
        pass

    @staticmethod
    def sell_product(customer: object, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
