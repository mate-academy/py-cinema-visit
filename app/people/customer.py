class Customer:
    def __init__(self, name: str, food: list) -> None:
        self.name = name
        self.food = food

    def wath_movies(self, movie: list) -> None:
        print(f'{self.name} is watching "{movie}".')
