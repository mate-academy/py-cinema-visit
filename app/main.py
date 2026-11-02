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

    session_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    session_cleaner = Cleaner(cleaner)
    session_hall = CinemaHall(hall_number)

    for session_customer in session_customers:
        CinemaBar.sell_product(session_customer, session_customer.food)

    session_hall.movie_session(movie, session_customers, session_cleaner)
