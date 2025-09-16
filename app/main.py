# main.py

from app.Cinema.bar import CinemaBar
from app.people.customer import Customer
from app.Cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
    movie: str, customers: list[dict], hall_number: int, cleaner: str
) -> None:
    customer_objects = [
        Customer(c["name"], c["food"]) for c in customers
    ]
    for cust in customer_objects:
        CinemaBar.sell_product(cust.food, cust)
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    hall.movie_session(movie, customer_objects, staff)
