from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    all_customers = [Customer(someone["name"], someone["food"])
                     for someone in customers]
    for someone in all_customers:
        CinemaBar().sell_product(someone, someone.food)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, all_customers, Cleaner(cleaner))
