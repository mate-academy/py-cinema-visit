from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_class = [Customer(cus["name"], cus["food"]) for cus in customers]
    for customer in customers_class:
        CinemaBar.sell_product(customer, customer.food)
    ch = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    ch.movie_session(movie, customers_class, cleaner)
