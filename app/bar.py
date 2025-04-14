from __future__ import annotations


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name


class CinemaBar:
    @staticmethod
    def sell_product(
        customers: list[Customer], product: str, customer: Customer = None
    ) -> None:
        if customer:
            print(f"Cinema bar sold {product} to {customer.name}.")
        else:
            print(f"Cinema bar sold {product} to multiple customers.")
