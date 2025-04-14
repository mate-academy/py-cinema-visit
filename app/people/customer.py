class Customer:
    customers = []

    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food
        Customer.customers.append({"name": self.food, "food": self.food})

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
