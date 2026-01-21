class Customer:
    def __init__(self, name: str) -> None:
        self.name = name


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
