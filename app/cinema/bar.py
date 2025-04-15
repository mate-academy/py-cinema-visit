from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: "Customer") -> None:
        print(f"Cinema bar.py sold {product} to {customer.name}.")
