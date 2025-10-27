from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    new_customers = [Customer(**customer) for customer in customers]
    for person in new_customers:
        CinemaBar.sell_product(person, person.food)

    CinemaHall(hall_number).movie_session(
        movie,
        new_customers,
        Cleaner(cleaner)
    )
