from app.people.customer import Customer


class CinemaBar:
    def sell_product(self, product: str, customer: Customer) -> None:
        self.customer = customer
        self.product = product
        print(f"Cinema bar sold {self.product} to {customer.name}.")
