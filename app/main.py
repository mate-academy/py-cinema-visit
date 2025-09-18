from __future__ import annotations
from typing import Iterable, Union

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def _as_customer(obj: Union[Customer, dict]) -> Customer:
    if isinstance(obj, Customer):
        return obj
    # Esperado: dict com chaves 'name' e 'food'
    return Customer(name=obj['name'], food=obj['food'])


def _as_cleaner(obj: Union[Cleaner, str, dict]) -> Cleaner:
    if isinstance(obj, Cleaner):
        return obj
    if isinstance(obj, str):
        return Cleaner(name=obj)
    # Se vier dict com 'name'
    return Cleaner(name=obj['name'])


def cinema_visit(
    movie: str,
    customers: Iterable[Union[Customer, dict]],
    hall_number: int,
    cleaner: Union[Cleaner, str, dict],
) -> None:
    # Construir UMA lista reutilizável de customers
    customer_list = [_as_customer(customer) for customer in customers]

    # Usar a classe diretamente (não instanciar CinemaBar)
    for customer in customer_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Reusar customer_list na sessão do hall
    cleaner_obj = _as_cleaner(cleaner)
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaner_obj,
    )
