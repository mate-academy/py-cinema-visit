from app.people.customer import Customer


class CinemaBar:
    pass

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
