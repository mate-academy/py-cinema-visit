class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def __repr__(self) -> str:
        return self.name

    def watch_movie(self, movie: str) -> None:
        print(f'{self} is watching "{movie}".')
