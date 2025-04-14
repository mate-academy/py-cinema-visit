"""
customer.py - inside this module create Customer class, its __init__ method
 takes and stores name, food - food that customer wants to buy in cinema bar.
 This class should have only one method watch_movie, this method takes movie
 and prints what movie customer is watching.
bob = Customer(name="Bob", food="popcorn")
bob.watch_movie(movie="Madagascar")
    # Bob is watching "Madagascar".
"""


class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
