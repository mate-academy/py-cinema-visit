from app.people.customer import Customer


class CinemaBar:
    """Class describes work of cinema bar"""

    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        """Method prints what product and to whom cinema sold"""
        print(f"Cinema bar sold {product} to {customer.name}.")
