from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        if isinstance(customer, Customer):
            print(f"Cinema bar sold {product} to {customer.name}.")
        else:
            print(f"Cinema bar sold {product} to {customer}.")
