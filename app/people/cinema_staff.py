# cinema_staff.py

class Cleaner:
    def __init__(self, name: str):
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"{self.name} is cleaning hall {hall_number}.")
