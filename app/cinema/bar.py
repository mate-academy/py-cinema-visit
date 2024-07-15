class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: dict) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
