from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer.food, customer)
    CinemaHall.movie_session(hall, movie, customers, cleaner)
