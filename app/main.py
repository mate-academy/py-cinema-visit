# app/main.py

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from typing import List, Dict


def cinema_visit(
    customers: List[Dict],
    hall_number: int,
    cleaner: str,
    movie: str
):
    # Cria instâncias de Customer
    customer_objects = [
        Customer(name=c['name'], food=c['food'])
        for c in customers
    ]

    # Vende produtos no cinema bar
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Cria instância de CinemaHall
    hall = CinemaHall(hall_number=hall_number)
    # Cria instância de Cleaner
    cleaning_staff = Cleaner(name=cleaner)

    # Inicia sessão de cinema
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
