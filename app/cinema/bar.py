from app.people.customer import Customer


class CinemaBar:

    @classmethod
    def sell_product(cls, product: str, customer: str | Customer) -> None:
        if isinstance(customer, str):
            print(f"Cinema bar sold {product} to {customer}.")
        else:
            print(f"Cinema bar sold {product} to {customer.name}.")
