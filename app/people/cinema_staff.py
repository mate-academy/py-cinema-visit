class Cleaner:
    """
    A class representing a cleaner in the cinema.

    Attributes:
        name (str): The name of the cleaner.

    Methods:
        clean_hall(hall_number: int) -> None:
            Prints a message that the cleaner is cleaning a specific hall.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a Cleaner with the specified name.

        Args:
            name (str): The name of the cleaner.
        """
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """
        Prints a message that the cleaner is cleaning the specified hall.

        Args:
            hall_number (int): The number of the hall to be cleaned.
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
