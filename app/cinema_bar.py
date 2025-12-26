class CinemaBar:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    @staticmethod
    def sell_product(customer, product, menu):
        if product in menu:
            print(f"{customer['name']} bought {product}.")
        else:
            print(f"{product} is not available.")