class Customer:
    def __init__(self, name: str, food: str):
        self.name = name
        self.food = food


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer):
        print(f"{customer.name} bought {product}")

customer = Customer("Bob", "popcorn")

CinemaBar.sell_product(product=customer.food, customer=customer)

