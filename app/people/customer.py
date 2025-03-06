class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food  # Виправлено: foof -> food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching \"{movie}\".')
