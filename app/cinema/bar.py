from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: "Customer | str") -> None:
        # accept either a Customer instance or a customer's name string
        customer_name = getattr(customer, "name", customer)
        print(f"Cinema bar sold {product} to {customer_name}.")
