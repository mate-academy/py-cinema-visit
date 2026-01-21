from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customers = [Customer(customer["name"], customer["food"])
                 for customer in customers]

    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)

    cleaning_staff = Cleaner(cleaner)
    c_h_inst = CinemaHall(hall_number)

    CinemaHall.movie_session(
        c_h_inst,
        movie_name=movie,
        customers=customers,
        cleaning_staff=cleaning_staff
    )
