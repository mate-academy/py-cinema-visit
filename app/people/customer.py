class Customer:
    def __init__(self, name: str = None, food: str = None) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching \"{movie}\".')
