from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str) -> None:

    customer_objs = [Customer(c["name"], c["food"]) for c in customers]
    cleaner_obj = Cleaner(cleaner)
    CinemaBar().multiple_sales(customer_objs)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_objs, cleaner_obj)
