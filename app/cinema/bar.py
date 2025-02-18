from app.people.customer import Customer

class CinemaHall:

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer}")


