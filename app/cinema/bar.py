class CinemaBar:
    @staticmethod
    def sell_product(product, customer):
        print(f"Cinema bar sold {product} to {customer.name}.")

class Customer:
    def __init__(self, name, food):
        self.name = name
        self.food = food
