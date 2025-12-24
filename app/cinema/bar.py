from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        if not isinstance(customer, Customer):
            raise ValueError
        print(f"Cinema bar sold {product} to {customer.name}.")
