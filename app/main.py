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
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    customers_objects = [Customer(**customer) for customer in customers]

    for customer in customers_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customers_objects,
        cleaning_staff=cleaner_obj
    )
