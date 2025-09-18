# app/cinema/hall.py
from typing import Iterable

class CinemaHall:
    """Sala de cinema (compatível com os testes)."""

    def __init__(self, number: int, capacity: int = 100) -> None:
        self.number = number
        self.capacity = capacity

    def movie_session(self, movie_name: str, customers: Iterable, cleaner) -> None:
        # 1) início da sessão
        print(f"\"{movie_name}\" started in hall number {self.number}.")
        # 2) cada cliente assistindo
        for c in customers:
            print(f"{c.name} is watching \"{movie_name}\".")
        # 3) fim da sessão
        print(f"\"{movie_name}\" ended.")
        # 4) limpeza
        print(cleaner.clean(self))
