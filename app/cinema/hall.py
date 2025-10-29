from typing import List
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    """
    Descreve as ações que ocorrem durante uma sessão de cinema
    em um corredor específico.
    """
    def __init__(self, hall_number: int) -> None:
        # Armazena APENAS o número do corredor.
        self.number = hall_number

    def movie_session(self, movie_name: str,
                      customers: List[Customer],
                      cleaning_staff: Cleaner) -> None:
        """
        Gerencia e registra o início, a exibição, o fim do filme e
        a limpeza do corredor.
        """
        # 1. Início do filme
        print(f'\"{movie_name}\" started in hall number {self.number}.')

        # 2. Clientes assistem ao filme
        for customer in customers:
            customer.watch_movie(movie=movie_name)

        # 3. Fim do filme
        print(f'\"{movie_name}\" ended.')

        # 4. Limpeza do corredor
        cleaning_staff.clean_hall(hall_number=self.number)
