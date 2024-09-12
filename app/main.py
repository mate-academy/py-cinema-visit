from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str,
) -> None:
    customers = [Customer(**customer) for customer in customers]
    cleaner = Cleaner(cleaning_staff)

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()

    for customer in customers:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie_name, customers, cleaner)
