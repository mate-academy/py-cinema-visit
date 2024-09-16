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

    hall_number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers = [Customer(**customer) for customer in customers]

    for customer in customers:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall_number.movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=cleaner
    )
