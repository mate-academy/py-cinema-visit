from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers = [Customer(**customer) for customer in customers]
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)

    hall.movie_session(movie, customers, cleaner)
