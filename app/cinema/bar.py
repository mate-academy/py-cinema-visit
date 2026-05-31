from typing import Any


class CinemaBar:
    @staticmethod
    def sell_product(customer: Any, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
