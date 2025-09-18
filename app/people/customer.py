from __future__ import annotations

from app.cinema.bar import CinemaBar  # only for type hints


class Customer:
    """Representa um cliente do cinema."""

    def __init__(self: 'Customer', name: str, food: str, balance: int = 0) -> None:
        self.name: str = name
        self.balance: int = balance
        self.food: str = food  # item de comida comprado (opcional)

    def watch(self: 'Customer', movie_name: str) -> None:
        print(f'{self.name} is watching "{movie_name}".')

    def watch_movie(self: 'Customer', movie_name: str) -> None:
        self.watch(movie_name)

    def buy_food(self: 'Customer', cinema_bar: CinemaBar, product: str) -> None:
        cinema_bar.sell_product(customer=self, product=product)
