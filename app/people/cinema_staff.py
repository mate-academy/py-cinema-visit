class Cleaner:
    def __init__(self, name: str) -> callable:
        self.name = name

    def clean_hall(self, hall_number: int) -> callable:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
