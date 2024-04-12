from typing import Any


class Cleaner:
    def __init__(self, name: Any) -> None:
        self.name = name

    def clean_hall(self, hall_number: Any) -> Any:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
