from app.people.customer import Customer


class CinemaBar:
    @classmethod
    def sell_product(cls, product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
