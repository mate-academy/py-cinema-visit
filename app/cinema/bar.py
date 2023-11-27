from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: int, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
