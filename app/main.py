# app/main.py

from __future__ import annotations
from typing import Iterable, Union

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def _as_customer(obj: Union[Customer, dict]) -> Customer:
    if isinstance(obj, Customer):
        return obj
    # Os testes passam dicts com 'name' e 'food'
    return Customer(name=obj['name'], food=obj['food'])


def _as_cleaner(obj: Union[Cleaner, str, dict]) -> Cleaner:
    if isinstance(obj, Cleaner):
        return obj
    if isinstance(obj, str):
        return Cleaner(name=obj)
    return Cleaner(name=obj['name'])


# >>> MUITO IMPORTANTE <<<
# A ORDEM de argumentos deve bater com tests/test_main.py:
# cinema_visit(customers, hall_number, cleaner, movie)
def cinema_visit(
    customers: Iterable[Union[Customer, dict]],
    hall_number: int,
    cleaner: Union[Cleaner, str, dict],
    movie: str,
) -> None:
    # Normaliza clientes (lista de Customer)
    customer_list = [_as_customer(c) for c in customers]

    # Vende no bar com método de instância (os testes instanciam a classe)
    bar = CinemaBar()
    for customer in customer_list:
        bar.sell_product(customer=customer, product=customer.food)

    # Roda a sessão no hall
    cleaner_obj = _as_cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_list, cleaner_obj)
