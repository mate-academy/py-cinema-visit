class CinemaBar:
    def sell_product(
        self,
        customer: object = None,
        product: str = None,
        customer_name: str = None
    ) -> None:
        if customer is not None and hasattr(customer, "name"):
            print(f"Cinema bar sold {product} to {customer.name}.")
        else:
            print(f"Cinema bar sold {customer} to {product}.")
