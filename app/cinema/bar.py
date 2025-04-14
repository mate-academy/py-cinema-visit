from app.people.customer import Customer


class CinemaBar:
    """Describes work of cinema bar"""

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """Prints what product and to whom cinema sold"""
        print(f"Cinema bar sold {product} to {customer.name}.")
