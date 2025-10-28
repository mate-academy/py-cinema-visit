from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str
) -> None:
    new_customers = [Customer(**customer) for customer in customers]
    for person in new_customers:
        CinemaBar.sell_product(person.food, person)

    CinemaHall(hall_number).movie_session(
        movie,
        new_customers,
        Cleaner(cleaner)
    )
