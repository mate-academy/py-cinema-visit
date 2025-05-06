class Customer:


    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie):
        return f"{self.name} is watching \"{movie}\""

# bob = Customer(name="Bob", food="popcorn")
# print(bob.watch_movie(movie="Madagascar"))
# # Bob is watching "Madagascar".