from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        # The sell_product method sells a product to the customer
        # and displays which product was sold and to whom
        print(f"Cinema bar sold {product} to {customer.name}.")
