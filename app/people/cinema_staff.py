class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        num = hall_number
        return print(f"Cleaner {self.name} is cleaning hall number {num}.")
