from typing import Any


class CinemaBar:
    @staticmethod
    def sell_product(customer: Any, product: Any) -> Any:
        print(f"Cinema bar sold {product} to {customer.name}.")
