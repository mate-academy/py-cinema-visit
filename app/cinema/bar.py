from app.people.customer import Customer


class CinemaBar:
    def __init__(self) -> None:
        self.name = Customer

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
