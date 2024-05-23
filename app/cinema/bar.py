from typing import Any


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Any) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
