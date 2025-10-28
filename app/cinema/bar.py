class CinemaBar:
    @staticmethod
    def sell_product(
            product: str,
            customer: callable
    ) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
