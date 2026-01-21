from typing import Any


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Any) -> str:
        print(f"Cinema bar sold {product} to {customer.name}.")
