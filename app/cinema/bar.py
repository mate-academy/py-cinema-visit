from app.people.customer import Customer


class CinemaBar:
    def __init__(self) -> None:
        self.products = []

    def sell_product(self, customer: Customer, product: str) -> None:
        self.products.append(product)
        print(f"Cinema bar sold {product} to {customer.name}.")
