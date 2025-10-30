class Cleaner:
    def __init__(self, name: str) -> None:
        """Store cleaner name."""
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """Cleaner cleans hall."""
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
