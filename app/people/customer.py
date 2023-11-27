from __future__ import annotations


class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

# A requirement not specified in the task condition,
# but used in an automated test
    def __str__(self) -> str:
        return self.name

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
