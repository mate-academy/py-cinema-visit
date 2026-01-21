class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def __str__(self) -> str:
        return self.name

    def watch_movie(self, movie: str) -> None:
        print(f"""{self.name} is watching "{movie}".""")
