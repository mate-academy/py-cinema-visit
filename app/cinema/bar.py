from app.people.customer import Customer  # noqa: F401


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
