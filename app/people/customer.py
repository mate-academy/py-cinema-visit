class Customer:

    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """Prints what movie customer is watching."""

        print(f'{self.name} is watching "{movie}".')
