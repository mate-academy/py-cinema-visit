class CinemaBar:
    @staticmethod
    def sell_product(customer: "Customer", product: "Customer.food") -> None:
        print(f"Cinema bar sold {product} to {customer}")
