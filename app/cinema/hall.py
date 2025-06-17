from typing import List
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    # Classe para a sala de cinema
    def __init__(self, hall_number: int) -> None:
        # Guarda o número da sala
        self.hall_number = hall_number

    def movie_session(
        self, movie_name: str, customers: List[Customer], cleaning_staff: Cleaner
    ) -> None:
        # Inicia o filme, faz clientes assistirem, termina o filme e limpa a sala
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.hall_number)
