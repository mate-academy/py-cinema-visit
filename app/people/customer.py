class Customer:
    """Class representing a cinema customer."""

    def __init__(self, name: str, food: str) -> None:
        """
        Initialize customer with name and desired food.

        Args:
            name: customer's name
            food: food that customer wants to buy in cinema bar
        """
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """
        Customer watches the movie.

        Args:
            movie: name of the movie
        """
        print(f"""{self.name} is watching "{movie}".""")
