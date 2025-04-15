class Cleaner:

    def __init__(self, name: str) -> None:
        """
        Initializes a cleaner.

        Parameters:
        name (str): The name of the cleaner.
        """
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """
        Cleans the cinema hall.

        Parameters:
        hall_number (int): The hall number to be cleaned.
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
