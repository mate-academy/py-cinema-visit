from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers = [Customer(customer["name"], customer["food"])
                 for customer in customers]
    hall = CinemaHall(hall_number)
    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers, Cleaner(cleaner))
