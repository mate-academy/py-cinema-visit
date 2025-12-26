from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    cb = CinemaBar()
    for cust in customers:
        cb.sell_product(cust, cust.food)
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers, cleaner)
