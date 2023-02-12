class Cleaner:
    staff = []

    def __init__(self, name: str) -> None:
        self.name = name
        Cleaner.staff = self

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
