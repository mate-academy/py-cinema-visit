

class Customer:
    """
    Represents a customer with their name
    and food preferences.

    This class is used to model a customer
    with attributes for their name and
    preferred food. It includes functionality
    for associating a customer with a movie
    they are watching.

    """
    def __init__(self, name: str, food: str) -> None:
        """
        Initializes an instance of the class with
        a name and favorite food.

        :param name: Name of the individual
        :type name: str
        :param food: Favorite food of the individual
        :type food: str
        """
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """
        Watches a movie and prints a message indicating
        that the user is watching the movie.

        :param movie: The name of the movie to watch.
        :type movie: str
        :return: None
        """
        print(f'{self.name} is watching "{movie}".')
