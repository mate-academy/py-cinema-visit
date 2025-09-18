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
    return Cleaner(name=obj['name'])


def _normalize_customers(
    customers: Union[Iterable[Union[Customer, dict]], Customer, dict, int, str, bytes]
) -> list[Customer]:
    # Caso único objeto válido
    if isinstance(customers, (Customer, dict)):
        return [_as_customer(customers)]
    # Strings/bytes não são coleções válidas aqui
    if isinstance(customers, (str, bytes)):
        raise TypeError(
            'customers must be an iterable of Customer or dict, not a string/bytes'
        )
    # Ints (erro reportado no CI)
    if isinstance(customers, int):
        raise TypeError(
            'customers must be an iterable of Customer or dict, not an int'
        )
    # Iterável “normal”
    try:
        return [_as_customer(c) for c in customers]  # type: ignore[arg-type]
    except TypeError as exc:
        # Captura casos “não iteráveis” customizados
        raise TypeError(
            'customers must be an iterable of Customer or dict'
        ) from exc


def cinema_visit(
    movie: str,
    customers: Union[Iterable[Union[Customer, dict]], Customer, dict, int, str, bytes],
    hall_number: int,
    cleaner: Union[Cleaner, str, dict],
) -> None:
    customer_list = _normalize_customers(customers)

    # Usar a classe diretamente (não instanciar CinemaBar)
    for customer in customer_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cleaner_obj = _as_cleaner(cleaner)
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaner_obj,
    )
