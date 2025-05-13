from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: Customer) -> str:
        return print(f"Cinema bar sold {product} to {customer.name}.")
