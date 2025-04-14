class Customer:
    # customers = []
    def __init__(self, name, food):
        self.name = name
        self.food = food
        # Customer.customers.append(self)

    def watch_movie(self, movie):
        print(f'{self.name} is watching "{movie}".')
