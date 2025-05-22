class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.food = food
        self.name = name

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
