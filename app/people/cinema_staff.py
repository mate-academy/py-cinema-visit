class Cleaner:
    def __init__(self: "Cleaner", name: str) -> None:
        self.name = name

    def clean_hall(self: "Cleaner", hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
