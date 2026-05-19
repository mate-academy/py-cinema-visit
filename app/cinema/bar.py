from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        name = customer.name if hasattr(customer, "name") else customer
        print(f"Cinema bar sold {product} to {name}.")
