from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from typing import List, Dict


def cinema_visit(
    movie: str,
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str
) -> None:
    # створюємо об'єкти Customer
    customer_objects = [
        Customer(name=customer_data["name"], food=customer_data["food"])
        for customer_data in customers
    ]

    # продаємо їжу через CinemaBar
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # створюємо CinemaHall
    hall = CinemaHall(hall_number=hall_number)

    # створюємо Cleaner
    cleaning_staff = Cleaner(name=cleaner)

    # запускаємо сеанс
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
