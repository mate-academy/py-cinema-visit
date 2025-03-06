from app.people.customer import Customer


class CinemaBar:

    def sell_product(self, product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}")
