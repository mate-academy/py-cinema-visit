class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f"{self.name} is watching \"{movie}\".")


if __name__ == "__main__":
    bob = Customer(name="Bob", food="popcorn")
    bob.watch_movie(movie="Madagascar")
    # Bob is watching "Madagascar".
