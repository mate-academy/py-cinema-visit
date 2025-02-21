from typing import Callable


class CinemaBar:
    @staticmethod
    def sell_product(customer: Callable, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
