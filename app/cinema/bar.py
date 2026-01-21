from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        customer_order = Customer(customer.name, product)
        print(
            f"Cinema bar sold {customer_order.food} to {customer_order.name}."
        )
