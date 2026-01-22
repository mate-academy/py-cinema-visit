class CinemaBar:
    def __init__(self) -> None:
        pass

    @staticmethod
    def sell_product(product: str, customer: type) -> str:
        print(f"Cinema bar sold {product} to {customer.name}.")
