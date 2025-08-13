from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from typing import List, Dict


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    # Создаём объекты Customer
    customer_objects = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    # Продажа еды через CinemaBar
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Создаём объект CinemaHall
    hall = CinemaHall(number=hall_number)

    # Создаём объект Cleaner
    cleaning_staff = Cleaner(name=cleaner)

    # Проведение сеанса
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
