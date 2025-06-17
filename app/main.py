from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[Dict[str, str]], hall_number: int, cleaner: str, movie: str
) -> None:
    # Cria clientes a partir da lista de dicionários
    customer_instances = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    # Cria sala de cinema e faxineiro
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    # Vende comida para cada cliente
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Executa a sessão de filme
    hall.movie_session(
        movie_name=movie, customers=customer_instances, cleaning_staff=cleaning_staff
    )
