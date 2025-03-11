class Cleaner:
    def __init__(self, name: str):
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f'Cleaner {self.name} is cleaning hall number {hall_number}.')
