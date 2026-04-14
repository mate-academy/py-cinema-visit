class Customer:
    def __init__(self, food: str, name: str) -> None:
        self.food = food
        self.name = name

    def watch_movie(self, movie: str):
        print(f'{self.name} is watching \"{movie}\".')
