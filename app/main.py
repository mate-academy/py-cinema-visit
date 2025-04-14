from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cst_in = [Customer(cst["name"], cst["food"]) for cst in customers]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(cleaner)
    for customer in cst_in:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, cst_in, cinema_cleaner)
