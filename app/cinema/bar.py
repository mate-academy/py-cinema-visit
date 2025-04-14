from ..people import customer as cst


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: cst.Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
