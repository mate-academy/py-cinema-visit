from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    patrons = [Customer(**patron) for patron in customers]

    concessions = CinemaBar()
    for patron in patrons:
        concessions.sell_product(patron.food, patron)

    cleaning_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, patrons, cleaning_staff)
