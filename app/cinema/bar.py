from __future__ import annotations
class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: Customer):
        print(f"Cinema bar sold {product} to {customer.name}")
