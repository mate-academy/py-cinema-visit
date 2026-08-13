from app.people.customer import Customer


class CinemaBar:
    def __init__(self):
        pass

    @staticmethod
    def sell_product(product: str, customer: "Customer"):
        print(f"Cinema bar sold {product} to {customer.name}.")
