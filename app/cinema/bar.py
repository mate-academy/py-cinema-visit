import app.people.customer as customer_md


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: customer_md.Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")