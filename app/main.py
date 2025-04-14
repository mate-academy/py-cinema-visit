from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    people = [Customer(person["name"], person["food"]) for person in customers]

    [CinemaBar.sell_product(person.food, person) for person in people]
    CinemaHall(hall_number).movie_session(movie, people, Cleaner(cleaner))
