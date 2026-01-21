from app.people import customer


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: customer.Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
