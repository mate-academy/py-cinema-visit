class Customer:
    customers = []

    def __init__(self, name: str, food: str):
        self.name = name
        self.food = food
        self.customers.append(self)

    def watch_movie(self, movie: str):
        print(f'{self.name} is watching "{movie}".')
