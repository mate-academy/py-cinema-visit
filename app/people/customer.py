class Customer:

    def __int__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f"{self.name} is watching \"{movie}\".")
