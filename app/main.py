from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers = [Customer(**customer) for customer in customers]
    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers, hall_cleaner)
