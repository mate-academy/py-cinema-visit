from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: str | Customer) -> None:
        if isinstance(customer, Customer):
            customer = customer.name
        print(f"Cinema bar sold {product} to {customer}.")
