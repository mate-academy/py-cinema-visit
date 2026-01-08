class Cleaner:
    """
    Represents a cinema staff member responsible for cleaning a certain hall.

    Args:
        name (str): The name of the cleaner.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """
        Call the cleaner on duty to clean the given hall.

        Args:
            hall_number (int): the hall that needs to be cleaned.
        """

        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
