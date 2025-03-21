class Customer:
    def __init__(self, name: str, food: str, movie: str = None) -> None:
        self.name = name
        self.food = food
        self.movie = movie

    def watch_movie(self, movie: str) -> None:
        print(f"{self.name} is watching {movie}")
