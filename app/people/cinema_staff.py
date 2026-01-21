class Cleaner:
    def __init__(self, name: str | object) -> None:
        self.name = name

    def clean_hall(self, hall_number: int | object) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
