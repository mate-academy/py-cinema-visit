from app.bar import CinemaBar
from app.hall import CinemaHall
from app.customer import Customer
from app.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for data in customers:
        customer = Customer(**data)
        cinema_hall.movie_session(movie, [customer], cleaning_staff)
