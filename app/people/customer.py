class Customer:
    def __init__(self, name: str, food: str) -> None:
        """
        Initializes a customer with their name and chosen food.
        """
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """
        Prints the movie the customer is currently watching.
        """
        print(f'{self.name} is watching "{movie}".')
