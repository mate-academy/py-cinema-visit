# app/people/cinema_staff.py


class Cleaner:
    def __init__(self, name: str) -> None:
        """Initialize with cleaner's name."""
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """Simulate cleaning a hall."""
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
