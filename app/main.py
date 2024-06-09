from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie_name: str
) -> None:
    # Створення екземплярів клієнтів
    customer_objects = [Customer(**customer) for customer in customers]

    # Створення екземпляра CinemaBar
    cinema_bar = CinemaBar()

    # Продаж продуктів клієнтам
    for customer in customer_objects:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    # Створення екземпляра CinemaHall
    hall = CinemaHall(hall_number)

    # Створення екземпляра Cleaner
    cleaner_obj = Cleaner(cleaner)

    # Проведення сеансу фільму
    hall.movie_session(movie_name, customer_objects, cleaner_obj)
