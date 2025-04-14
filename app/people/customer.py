from typing import Any


class Customer:
    def __init__(self, name: Any, food: Any) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: Any) -> Any:
        print(f'{self.name} is watching \"{movie}\".')
