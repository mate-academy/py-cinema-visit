from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: int) -> None:
        customer.food = product
        print(f"Cinema bar sold {customer.food} to {customer.name}.")
