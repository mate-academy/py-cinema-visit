from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str):
    customers = [Customer(customer["name"], customer["food"]) for customer in customers]
    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall = CinemaHall(hall_number)
    cleaners = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers, cleaners)