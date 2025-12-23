class Customer:

    def __init__(self, name: str, food: str | None) -> None:
        self.name: str = name
        self.food: str | None = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
