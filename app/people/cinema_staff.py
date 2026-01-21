class Cleaner:

    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        cleaner = self.name
        print(f"Cleaner {cleaner} is cleaning hall number {hall_number}.")
