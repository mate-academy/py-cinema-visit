from app.people.customer import Customer


class CinemaBar:
    """
    Describing bar work at cinema
    """

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
