from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_inst = [Customer(d["name"], d["food"]) for d in customers]
    cinemahall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for cust in customer_inst:
        CinemaBar.sell_product(cust, cust.food)

    cinemahall.movie_session(movie, customer_inst, cleaner)
