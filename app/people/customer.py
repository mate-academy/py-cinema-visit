from typing import List


class Customer:
    def __init__(self, name: str, food: str | List[str]) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
