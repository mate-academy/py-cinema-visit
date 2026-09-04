from app.people import customer as client


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: client.Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
