class Customer:
    def __init__(self, name, food) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')


if __name__ == '__main__':
    bob = Customer("Bob", "popcorn")
    bob.watch_movie("billy")
