from app.people import customer


class CinemaBar:

    @staticmethod
    def sell_product(customer: customer.Customer, product: str) -> None:
        # Cinema bar sold popcorn to Bob.
        return print(f"Cinema bar sold {product} to {customer}.")
