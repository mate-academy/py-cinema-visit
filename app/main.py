from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    bar_module = CinemaBar()
    for customer in customers:
        bar_module.sell_product(customer["name"], customer["food"])
    hall_module = CinemaHall(hall_number)
    staff_module = Cleaner(cleaner)
    hall_module.movie_session(movie, customers, staff_module)
