from typing import List, Dict

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: List[Dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    people = [
        Customer(name=customer["name"],
                 food=customer["food"]) for customer in customers
    ]
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaner)

    for person in people:
        cinema_bar.sell_product(person, person.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=people,
        cleaning_staff=cleaner
    )
