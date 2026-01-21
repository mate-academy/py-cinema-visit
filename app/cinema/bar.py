from app.people.customer import Customer  # for using Customer annotation


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
#  sells a product to the customer and displays which product was sold
