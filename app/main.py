from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    cb = CinemaBar()
    ch = CinemaHall(hall_number)
    customers = [Customer(customer["name"], customer["food"])
                 for customer in customers]
    for customer_person in customers:
        cb.sell_product(customer_person, customer_person.food)
    ch.movie_session(movie, customers, Cleaner(cleaner))
