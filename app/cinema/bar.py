class CinemaBar:
    def __init__(self, product: str = None, customer: str = None) -> None:
        self.product = product
        self.customer = customer

    def sell_product(self) -> str:
        return f"Cinema bar sold {self.product} to {self.customer}."

