from app.people.customer import Customer


class CinemaBar:
    def __init__(self: int) -> None:
        pass

    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        result = f"Cinema bar sold {product} to {customer.name}."
        print(result)
