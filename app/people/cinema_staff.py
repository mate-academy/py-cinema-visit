class Cleaner:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def clean_hall(self, hall_number: int) -> None:
        self.hall_number = hall_number
        print(f"Cleaner {self.name} is cleaning" f" hall number {self.hall_number}.")

