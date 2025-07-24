from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_new = [
        Customer(**item) for item in customers
    ]
    cleaning_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_new,
        cleaning_staff=cleaning_staff
    )
