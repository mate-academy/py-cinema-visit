class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer) -> None:
        """
        Sells a product to a customer and prints the transaction.
        """
        print(f"Cinema bar sold {product} to {customer.name}.")
