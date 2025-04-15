class Customer:

    def __init__(self, name: str, food: str) -> None:
        """
        Initializes a customer.

        Parameters:
        name (str): The name of the customer.
        food (str): The food item the customer has.
        """
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """
        Simulates the action of a customer watching a movie.

        Parameters:
        movie (str): The name of the movie being watched.
        """
        print(f'{self.name} is watching "{movie}".')
