from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[Customer],
    hall_number: int,
    cleaner: Cleaner,
    movie: str
) -> None:
    customer_objects = [Customer(cs["name"], cs["food"]) for cs in customers]

    cinema_bar = CinemaBar()
    for cust in customers:
        cinema_bar.sell_product(cust["food"], cust["name"])

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie, customer_objects, cleaner_obj)
