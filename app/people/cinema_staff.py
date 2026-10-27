class Cleaner:
    def __init__(self, name: str) -> None:
        """
        Initializes a cleaner with their name.
        """
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """
        Prints that the cleaner is cleaning a specific hall.
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
