from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list | Customer,
        hall_number: int | CinemaHall,
        cleaner_name: str | Cleaner,
        movie: str | Customer
) -> None:
    for person in customers:
        CinemaBar.sell_product(person.get("food"), person.get("name"))
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers, cleaner_name)
