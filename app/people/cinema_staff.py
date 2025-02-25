from __future__ import annotations


class Cleaner:
    def __init__(self, name: str) -> Cleaner:
        self.name = name

    def clean_hall(self, hall_number: int) -> Cleaner:
        print(f'Cleaner {self.name} is cleaning hall number {hall_number}.')
