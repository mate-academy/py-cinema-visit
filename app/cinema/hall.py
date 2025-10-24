from typing import List


class Customer:
    """Descreve um cliente do cinema."""

    def __init__(self, name: str, food: str):
        self.name = name
        self.food = food

    def watch_movie(self, movie_name: str):
        """Simula o cliente assistindo ao filme."""
        print(f"{self.name} está assistindo {movie_name}.")


class Cleaner:
    """Descreve um membro da equipe de limpeza do cinema."""

    def __init__(self, name: str):
        self.name = name

    def clean_hall(self, hall_number: int):
        """Simula a limpeza da sala."""
        print(f"O limpador {self.name} está limpando a sala {hall_number}.")


# Classe principal
class CinemaHall:
    """Descreve as ações durante a sessão de cinema."""

    def __init__(self, hall_number: int):
        """Inicializa a sala de cinema com seu número."""
        self.number = hall_number

    def movie_session(self, movie_name: str, customers: List[Customer], cleaning_staff: Cleaner):
        """Gerencia uma sessão de cinema completa."""
        print(f"\n--- Sala {self.number}: O filme '{movie_name}' está começando. ---")

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f"--- Sala {self.number}: O filme '{movie_name}' terminou. ---")

        cleaning_staff.clean_hall(self.number)
        print("----------------------------------------------------------------")
