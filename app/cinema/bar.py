from app.people import customer as c


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: "c.Customer") -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
