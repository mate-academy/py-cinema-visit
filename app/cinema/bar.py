from __future__ import annotations

import app.people.customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str,
                     customer: app.people.customer.Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
