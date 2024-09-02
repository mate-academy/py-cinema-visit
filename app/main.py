from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str)\
        -> None:
    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for customer in customers:
        CinemaBar.sell_product(customer, product=customer.food)
    hall.movie_session(movie, customers, cinema_cleaner)
