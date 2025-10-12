from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: "Customer", product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
