from __future__ import annotations

class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: "Customer") -> None:
        print(f"{product} was sold to {customer.name}")
