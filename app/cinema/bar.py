from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        # Print which product was sold to which customer
        print(f"Cinema bar sold {product} to {customer.name}.")
