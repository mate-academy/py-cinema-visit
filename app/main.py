from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_list = [
        Customer(person["name"], person["food"])
        for person in customers
    ]

    for person in customers_list:
        CinemaBar().sell_product(person, person.food)

    CinemaHall(hall_number).movie_session(
        movie,
        customers_list,
        Cleaner(cleaner)
    )
