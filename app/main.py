from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    """Організовує відвідування кінотеатру клієнтами."""

    # Створюємо об'єкти клієнтів
    customer_objects = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    # Кожен клієнт купує їжу в кіно-барі
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Створюємо зал і прибиральника
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    # Проведення сеансу фільму
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
