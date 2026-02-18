from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    movie: str,
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
) -> None:

    customer_objs = [Customer(c["name"], c["food"]) for c in customers]
    cleaner_obj = Cleaner(cleaner)

    for customer_obj in customer_objs:
        CinemaBar().sell_product(customer_obj, customer_obj.food)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_objs, cleaner_obj)
