class CinemaBar:
    def __init__(self) -> None:
        pass

    @staticmethod
    def sell_product(product: str, customer: object) -> any:
        print(f"Cinema bar sold {product} to {customer.name}.")
