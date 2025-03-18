class Customer:
    def __init__(self, name: str, food: str) -> callable:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> callable:
        print(f'{self.name} is watching "{movie}".')
