from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: str, product: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
