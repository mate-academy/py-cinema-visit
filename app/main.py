from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str) -> None:
    list_customer = [Customer(customer["name"], customer["food"])
                     for customer in customers]
    cleaner = Cleaner(cleaner)
    for customer in list_customer:
        CinemaBar.sell_product(customer, customer.food)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, list_customer, cleaner)
