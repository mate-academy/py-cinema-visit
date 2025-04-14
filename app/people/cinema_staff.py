class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """
        A method for cleaning a cinema hall.

        Parameters:
        - hall_number: int, the number of the hall to be cleaned.

        Returns:
        None
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
