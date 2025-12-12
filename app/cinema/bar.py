from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: "Customer") -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
