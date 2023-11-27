class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: type) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
