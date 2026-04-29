from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str) -> None:

    custs = [Customer(i["name"], i["food"]) for i in customers]
    barr = CinemaBar()
    for i in custs:
        barr.sell_product(i, i.food)

    ha = CinemaHall(hall_number)
    cl = Cleaner(cleaner)
    ha.movie_session(movie, custs, cl)
