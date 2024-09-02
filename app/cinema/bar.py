from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        product = customer.food
        print(f"Cinema bar sold {product} to {customer.name}.")
