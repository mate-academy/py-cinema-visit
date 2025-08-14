class Cleaner:
    """Represents a cinema cleaner."""

    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """Display cleaning action for a hall."""
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
