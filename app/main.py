from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall: int,
    cleaner: str,
    movie: str
) -> None:
    hall_inst = CinemaHall(hall)
    cleaner_inst = Cleaner(cleaner)
    customers_inst = [Customer(c["name"], c["food"]) for c in customers]

    for customer in customers_inst:
        CinemaBar.sell_product(customer, customer.food)

    hall_inst.movie_session(movie, customers_inst, cleaner_inst)

