from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers = [Customer(value["name"], value["food"]) for value in customers]
    cleaner = Cleaner(cleaner)
    for person in customers:
        CinemaBar.sell_product(person, person.food)
    hall_number = CinemaHall(hall_number)
    hall_number.movie_session(movie, customers, cleaner)
