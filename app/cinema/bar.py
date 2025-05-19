from app.people.customer import Customer


class CinemaBar:
    # def __init__(self, product: str, customer: object) -> None:
    #     self.product = product
    #     self.customer = customer

    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
