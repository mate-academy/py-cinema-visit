# app/cinema/hall.py

from __future__ import annotations
from typing import Iterable

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    # Os testes chamam:
    #   CinemaHall(number=6)  (keyword)
    #   ch = CinemaHall(4)    (posicional)
    def __init__(self, number: int) -> None:
        self.number = number

    # Os testes chamam:
    #   ch.movie_session(movie_name, [customer1, customer2], cleaner)
    def movie_session(
        self,
        movie_name: str,
        customers: Iterable[Customer],
        cleaner: Cleaner,
    ) -> None:
        # Linha de início EXATA:
        # '"I\'m Robot" started in hall number 4.\n'
        print(f'"{movie_name}" started in hall number {self.number}.')

        # Clientes assistem (usa Customer.watch_movie com aspas no título)
        for customer in customers:
            customer.watch_movie(movie_name)

        # Linha de término EXATA:
        # '"I\'m Robot" ended.\n'
        print(f'"{movie_name}" ended.')

        # Limpeza EXATA:
        # 'Cleaner John is cleaning hall number 4.\n'
        cleaner.clean_hall(hall_number=self.number)
