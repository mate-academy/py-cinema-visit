from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        customer.food = product
        print(f"Cinema bar sold {customer.food} to {customer.name}.")
