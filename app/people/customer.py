class Customer:
    """
    A class representing a customer in the cinema.

    Attributes:
        name (str): The name of the customer.
        food (str): The food item the customer wants to buy.

    Methods:
        watch_movie(movie: str) -> None:
            Prints a message that the customer is watching a specified movie.
    """
    def __init__(self, name: str, food: str) -> None:
        """
        Initializes a Customer with the specified name and desired food.

        Args:
            name (str): The name of the customer.
            food (str): The food item the customer wants to buy.
        """
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """
        Prints a message that the customer is watching the specified movie.

        Args:
            movie (str): The name of the movie the customer is watching.
        """
        print(f'{self.name} is watching "{movie}".')
