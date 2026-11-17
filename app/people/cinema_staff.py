class Cleaner:

    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"{Cleaner.__name__} {self.name}"
              f" is cleaning hall number {hall_number}.")
