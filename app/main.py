from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    ls_customers = []
    for costumer in customers:
        obj_costumer = Customer(costumer["name"], costumer["food"])
        ls_customers.append(obj_costumer)
        CinemaBar.sell_product(obj_costumer, costumer["food"])
    cinema_start = CinemaHall(hall_number)
    cinema_start.movie_session(movie, ls_customers, Cleaner(cleaner))
