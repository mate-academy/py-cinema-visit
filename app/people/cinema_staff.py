class Cleaner:
    def __init__(self: None, name: str) -> None:
        self.name = name

    def __repr__(self: None) -> str:
        return f"{self.name}"

    def clean_hall(self: None, hall_number: int) -> None:
        print(f"Cleaner {self.name} "
              f"is cleaning hall number {hall_number}.")
