class CinemaBar:
    @staticmethod
    def sell_product(customer: object, product: str) -> None:
        if hasattr(customer, "name"):
            print(f"Cinema bar sold {product} to {customer.name}.")
        else:
            print(f"Cinema bar sold {product} to {customer}.")
