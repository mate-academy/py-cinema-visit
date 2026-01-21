# app/cinema/bar.py

from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """Sells a product to the given customer."""
        print(f"Cinema bar sold {product} to {customer.name}.")
