from __future__ import annotations


class Customer:
    """A class to represent a customer.

    :param name: The name of the customer.
    :type name: str
    :param food: The food the customer has.
    :type food: str
    """

    def __init__(self, name: str, food: str) -> None:
        """Initializes a Customer object.

        :param name: The name of the customer.
        :type name: str
        :param food: The food the customer has.
        :type food: str
        """
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """Makes the customer watch a movie.

        :param movie: The movie to watch.
        :type movie: str
        """
        print(f'{self.name} is watching "{movie}".')
