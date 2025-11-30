class Customer:
    peoples = []

    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food
        Customer.peoples.append(self)

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
