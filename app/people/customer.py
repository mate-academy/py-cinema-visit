class Customer:
    def __init__(self: 'Customer', name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self: 'Customer', movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
