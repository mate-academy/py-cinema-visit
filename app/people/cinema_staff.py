class Cleaner:
    """Class representing a cinema cleaner."""

    def __init__(self, name: str) -> None:
        """
        Initialize cleaner with name.

        Args:
            name: cleaner's name
        """
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """
        Cleaner cleans the specified hall.

        Args:
            hall_number: number of hall to clean
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
