class Cleaner:
    def __init__(self, name: str, hall_number: int) -> None:
        self.name = name
        self.hall_number = hall_number

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall {hall_number}.")