"""
customer.py

This module describes a cinema customer.
"""


class Customer:
    """Represents a customer visiting the cinema."""

    def __init__(self, name: str, food: str) -> None:
        """
        :param name: str, the name of the customer.
        :param food: str, the food that the customer wants to buy
        """
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """
        Print which movie the customer is watching.

        :param movie: str, the name of the movie being watched.
        """
        print(f'{self.name} is watching "{movie}".')
