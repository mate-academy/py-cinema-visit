class CinemaBar:
    """Class representing a cinema bar."""

    @staticmethod
    def sell_product(product: str, customer) -> None:
        """Sell a product to a customer."""
        print(f"Cinema bar sold {product} to {customer.name}.")
