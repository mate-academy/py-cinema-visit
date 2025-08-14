from app.people.customer import Customer


class CinemaBar:
    """Represents a cinema bar."""

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """Sell a product to a customer."""
        print(f"Cinema bar sold {product} to {customer.name}.")
