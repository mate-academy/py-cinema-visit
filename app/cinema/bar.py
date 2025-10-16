from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(customer: "Customer", product: str) -> None:
        message = f"Cinema bar sold {product} to {customer}."
        print(message)
