class Customer:
    def __init__(self: None, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def __repr__(self: None) -> str:
        return self.name

    def watch_movie(self: None, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
