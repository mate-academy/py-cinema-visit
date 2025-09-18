from __future__ import annotations
from typing import Iterable

from app.people.customer import Customer
from app.people.cinema_staff import CinemaStaff


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        # ✅ Somente hall_number armazenado
        self.hall_number = hall_number

    # ✅ Assinatura EXATA exigida
    def movie_session(self, movie_name: str, customers: Iterable[Customer], cleaning_staff: CinemaStaff) -> None:
        # ✅ Chama o método com keyword exatamente como descrito
        for customer in customers:
            customer.watch_movie(movie=movie_name)

        # ✅ Chama com keyword arg 'hall_number='
        cleaning_staff.clean_hall(hall_number=self.hall_number)
