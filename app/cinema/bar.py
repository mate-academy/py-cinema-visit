from app.people.customer import Customer


class CinemaBar:
    def sell_product(self, product: str, customer) -> None:

        if isinstance(customer, Customer):
            customer_name = customer.name
        else:
            customer_name = customer

        print(f"Cinema bar sold {product} to {customer_name}.")
