from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customer_objects = []
    for item in customers:
        customer = Customer(item["name"], item["food"])
        CinemaBar.sell_product(item["food"], customer)
        customer_objects.append(customer)
    staff = Cleaner(cleaner)
    ch = CinemaHall(hall_number)
    ch.movie_session(movie, customer_objects, staff)
