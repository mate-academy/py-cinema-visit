from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    clean = Cleaner(cleaner)
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(cust, customer["food"])
    cinema_hall.movie_session(movie, customers, clean)
