class Customer:
    """
    Represents a cinema customer with specific preferences.

    It stores the customer's name and their chosen food item,
    and handles the action of watching a movie.

    Args:
        name (str): The name of the customer.
        food (str): The food item the customer wants to buy.
    """

    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def __str__(self) -> str:
        return self.name

    def watch_movie(self, movie: str) -> None:
        """
        Shows which movie the customer is watching.

        Args:
            movie (str): The film chosen by the customer.
        """
        print(f'{self.name} is watching "{movie}".')
