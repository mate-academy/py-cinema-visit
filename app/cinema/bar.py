from app.people.customer import Customer


class CinemaBar:  # Class that represents cinema bar.
    @staticmethod
    # Static method that sells food to customer.
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
