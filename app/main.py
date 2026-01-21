from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customers = [Customer(**customer) for customer in customers]
    hall_event = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar

    for customer in customers:
        cinema_bar.sell_product(customer, customer.food)

    hall_event.movie_session(movie, customers, hall_cleaner)
