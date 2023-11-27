from app.people import Customer


class CinemaBar:

    @staticmethod
    def sell_product(
        product: str,
        customer: Customer
    ) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
