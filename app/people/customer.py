from __future__ import annotations


class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, move_name: str) -> None:
        print(f'{self.name} is watching "{move_name}".')
