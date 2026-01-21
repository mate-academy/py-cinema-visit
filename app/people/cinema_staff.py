class Cleaner:

    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """Prints that cleaner is cleaning hall with given number."""
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
