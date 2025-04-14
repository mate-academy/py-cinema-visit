from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


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
    session_hall = CinemaHall(hall_number)
    session_cleaner = Cleaner(cleaner)

    for customer in session_customers:
        CinemaBar.sell_product(customer.food, customer)

    session_hall.movie_session(movie, session_customers, session_cleaner)
