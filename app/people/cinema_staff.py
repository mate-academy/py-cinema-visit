# app/people/cinema_staff.py

class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        # Saída EXATA exigida:
        # "Cleaner Anatoly is cleaning hall number 9.\n"
        print(f'Cleaner {self.name} is cleaning hall number {hall_number}.')
