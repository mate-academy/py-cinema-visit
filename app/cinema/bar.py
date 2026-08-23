from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def __sell_product__(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}")
